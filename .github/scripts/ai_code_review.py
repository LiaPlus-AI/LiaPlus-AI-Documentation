import os
import subprocess
import json
from pathlib import Path
from openai import OpenAI
import re
from collections import defaultdict, Counter

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
OUTPUT_JSON = Path("ai_review_comments.json")


def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}\n{result.stderr.decode()}")
    return result.stdout.decode()


def get_base_branch():
    ref = os.environ.get("GITHUB_BASE_REF")
    return f"origin/{ref}" if ref else "HEAD^"


def get_changed_files():
    return run_command(["git", "diff", "--name-only", f"{get_base_branch()}...HEAD"]).splitlines()


def get_diff_with_line_numbers(file_path):
    return run_command(["git", "diff", "-U0", f"{get_base_branch()}...HEAD", "--", file_path])


def extract_position_map(diff_output):
    position_map = {}
    diff_lines = diff_output.splitlines()
    new_line_num = None
    diff_pos = 0

    for line in diff_lines:
        diff_pos += 1

        if line.startswith("@@"):
            match = re.match(r"@@ -\d+(?:,\d+)? \+(\d+)", line)
            if match:
                new_line_num = int(match.group(1))
            continue

        if line.startswith("+") and not line.startswith("+++"):
            if new_line_num is not None:
                position_map[new_line_num] = diff_pos
                new_line_num += 1
        elif not line.startswith("-"):
            if new_line_num is not None:
                new_line_num += 1

    return position_map


def summarize_comments(comments):
    file_set = set()
    severity_counts = defaultdict(int)
    keywords = Counter()

    for comment in comments:
        file_set.add(comment["path"])
        body = comment["body"].lower()

        if "**critical**" in body:
            severity_counts["Critical"] += 1
        elif "**warning**" in body:
            severity_counts["Warning"] += 1
        else:
            severity_counts["Info"] += 1

        # Extract common themes for better summary
        for keyword in [
            "refactor", "performance", "security", "redundant", "inconsistent", "naming", "formatting",
            "readability", "best practice", "bug", "error", "typo"
        ]:
            if keyword in body:
                keywords[keyword] += 1

    files_reviewed = ", ".join(f"`{f}`" for f in sorted(file_set))
    most_common = ", ".join(f"`{k}`" for k, _ in keywords.most_common(4))

    return f"""### 🤖 AI Code Review Summary

**Files reviewed:** {files_reviewed}  
**Total suggestions:** `{len(comments)}`  
**Severity:** 🚨 {severity_counts['Critical']} critical • ⚠️ {severity_counts['Warning']} warnings • ℹ️ {severity_counts['Info']} informational  

---

### 🔍 Highlights
- Reviewed `{len(file_set)}` modified files for code quality, consistency, and best practices.
- Common issues flagged: {most_common or "general formatting and maintainability improvements"}.
- Suggested improvements include refactoring redundant logic, applying consistent code styles, and fixing minor issues.

---

Click **“View reviewed changes”** to explore inline suggestions.
"""


def generate_ai_comments(file_path, diff_output):
    # Use dynamic configuration for model, temperature, and role from environment variables
    model = os.getenv("AI_MODEL", "gpt-4")
    temperature = float(os.getenv("AI_TEMPERATURE", "0.3"))
    role_config = os.getenv("CODE_REVIEW_ROLE", 
        "You are an expert code review assistant with focus on DRY principles, high-level quality, comprehensive edge case coverage, proper use of global functions and modular design. Ensure dynamic configuration usage instead of static values. Also verify adherence to naming conventions, documentation, secure coding practices, efficient error handling, performance optimizations, logging, and test coverage for overall maintainability and readability.")
    
    prompt = f'''
Please review the provided code diff file with an emphasis on:
- Complete code clean-up and removal of dead or redundant code.
- Adherence to DRY principles and promotion of modular design.
- High-level improvements in code quality, reusability, and maintainability.
- Comprehensive coverage of edge cases.
- Replacing any static values with dynamic configurations retrieved from the database or environment variables.
- Proper use of global functions, clear separation of concerns, and adherence to an appropriate project structure.
- Consistent naming conventions, clear documentation, and overall code readability.
- Efficient error handling and secure coding practices.
- Optimizing performance, ensuring scalability, and maintaining expected behavior.
- Ensuring appropriate logging, monitoring, and test coverage where applicable.
- Adherence to the Single Responsibility Principle and proper modularity.
- Validating all inputs to prevent data exposure and to ensure proper sanitization.
- Enforcement of authorization checks and secure handling of sensitive information.
- Verifying backward compatibility and reviewing dependency updates as well as new dependencies.
- Optimization of database queries or API calls where relevant.
- Checking and correcting grammar, punctuation, and spelling in PR comments, documentation, and in all strings within the PR.

Output your suggestions in this structured format:
### File: <file_path>
### Line: <line_number>
### Severity: <Critical | Warning | Info>
### Comment:
<Markdown explanation of the issue, its impact, and a high-level fix>
### Suggestion:
```suggestion
<Exact replacement code that GitHub can commit directly, with correct formatting>
```
Here is the diff:
{diff_output}
'''
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": role_config
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content


def severity_emoji(level):
    level = level.lower()
    if "critical" in level:
        return "\ud83d\udea8"
    if "warn" in level:
        return "\u26a0\ufe0f"
    return "\u2139\ufe0f"


def parse_ai_response_to_json(file_path, ai_output, position_map):
    issues = []
    blocks = ai_output.split("### File:")
    for block in blocks:
        if not block.strip():
            continue
        try:
            file_match = re.search(
                r"^(.*?)\n### Line: (\d+)\n### Severity: (.*?)\n### Comment:\n(.*?)\n### Suggestion:\n```suggestion\n(.*?)\n```",
                block, re.DOTALL
            )
            if file_match:
                path = file_match.group(1).strip()
                line_number = int(file_match.group(2).strip())
                severity = file_match.group(3).strip()
                body = file_match.group(4).strip()
                suggestion_code = file_match.group(5).strip()
                position = position_map.get(line_number)
                if position:
                    issues.append({
                        "path": path,
                        "position": position,
                        "body": f"{severity_emoji(severity)} **{severity}**\n\n{body}\n\n```suggestion\n{suggestion_code}\n```"
                    })
        except Exception as e:
            print(f"❌ Failed to parse block: {block[:100]}... | Error: {e}")
    return issues


def main():
    all_comments = []
    for file in get_changed_files():
        if file.endswith((".py", ".js", ".ts", ".java", ".go", ".cpp", ".c", ".cs", ".php")):
            diff = get_diff_with_line_numbers(file)
            if not diff.strip():
                continue
            position_map = extract_position_map(diff)
            ai_output = generate_ai_comments(file, diff)
            comments = parse_ai_response_to_json(file, ai_output, position_map)
            all_comments.extend(comments)

    summary = summarize_comments(all_comments)

    OUTPUT_JSON.write_text(json.dumps({
        "summary": summary,
        "comments": all_comments
    }, indent=2))

    print(f"✅ Structured comments and summary written to {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
