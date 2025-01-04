# LiaPlus AI

Welcome to the comprehensive guide for LiaPlus AI, your solution for revolutionizing customer service with AI Employees. This repository will help you explore our platform, its key capabilities, and features, and guide you through integration and deployment.

## About LiaPlus AI

LiaPlus AI empowers businesses across **India, UAE, Saudi Arabia, South Africa, and Australia** to enhance customer service using AI Employees. These AI-driven solutions deliver **real results**, transforming customer interactions by automating high-volume, routine tasks while enabling human employees to focus on more meaningful work.

## Why Choose LiaPlus AI?

Managing customer service is more challenging than ever, with shrinking teams and increasing demands. LiaPlus AI offers a sustainable, scalable solution by leveraging **Conversational AI** and **Generative AI** to:

- Handle millions of inquiries across 18+ languages.
- Perform tasks with **99.7% intent recognition accuracy**.
- Reduce workloads for human employees while enhancing customer satisfaction.

### What Can LiaPlus AI Do?
- **Voice & Chat Support:** Interact in multiple languages and across platforms.
- **Lead Qualification & Scheduling:** Qualify leads and book appointments instantly.
- **CRM Integration:** Seamlessly integrate with your backend systems for smooth task execution.
- **High Scalability:** Handle up to **5000 calls/hour** with 24/7 availability.

## Join Us in Shaping the Future

LiaPlus AI is driving the future of customer service. Become an early adopter of AI technology and empower your team with cutting-edge tools that redefine efficiency and customer satisfaction. Together, let’s create a seamless, scalable, and intelligent customer service experience.


----


# Transcriber

## Overview
LiaPlus AI supports multiple transcriber providers to ensure seamless and accurate transcription services. This section provides details on the supported providers and their configuration options.


## Supported Transcriber Providers

LiaPlus AI supports the following transcriber providers:

- **Deepgram**
- **Azure**
- **Gladia**

## Deepgram Transcriber

### Configuration Options
- **Language**
- **Model**

### Language and Model Options

#### **nova-2-general (default):**
- **Languages:**
  - English (Generic)
  - English (India)
  - English (United States)
  - English (Australia)
  - English (United Kingdom)
  - English (New Zealand)
  - Hindi
  - Malay

#### **nova-2-phonecall:**
- **Languages:**
  - English (Generic)
  - English (United States)

#### **nova-2-conversationalai:**
- **Languages:**
  - English (Generic)
  - English (United States)

#### **nova-phonecall:**
- **Languages:**
  - English (Generic)
  - English (United States)

#### **nova-general:**
- **Languages:**
  - English (Generic)
  - English (United States)
  - English (Australia)
  - English (United Kingdom)
  - English (New Zealand)
  - English (India)
  - Hindi


## Azure Transcriber

### Configuration Options
- **Model**
- **Language**

### Model Option
- **Azure Speech to Text**

### Language Options
Azure supports a wide range of languages, including:

- **Afrikaans (South Africa)**
- **Arabic (United Arab Emirates)**
- **Arabic (Egypt)** 
- **Arabic (Saudi Arabia)**
- **Bengali (India)** 
- **English (Australia)** 
- **English (United Kingdom)** 
- **English (India)** 
- **English (Singapore)** 
- **English (United States)** 
- **Hindi (India)** 
- **Marathi (India)** 
- **Malay (Malaysia)** 
- **isiZulu (South Africa)** 

## Gladia Transcriber

### Configuration Options
- **Language**
- **Model**

### Language and Model Options

#### **Fast Model:**
- **Languages:** Afrikaans, Arabic, Bengali, English, Hindi, Malay, Marathi, Zulu

#### **Accurate Model:**
- **Languages:** Afrikaans, Arabic, Bengali, English, Hindi, Malay, Marathi, Zulu

----

# LLM

## Overview
LiaPlus AI supports multiple LLM providers to ensure seamless natural language processing services. This section provides details on the supported providers and their configuration options.

## Supported LLM Providers

LiaPlus AI supports the following LLM providers:

- **OpenAI**
- **Azure OpenAI**
- **Anthropic** (Coming Soon)
- **Groq** (Coming Soon)

## OpenAI LLM

### Configuration Options
- **Model name**

### Model Options
- **GPT 4**
- **GPT-4 0**
- **GPT 4 (1106)**
- **GPT 4 (32K)**
- **GPT 3.5 Turbo (1106)**
- **GPT 3.5 Turbo (0613-16K)**


## Azure OpenAI LLM

### Configuration Options
- **Model name**

### Model Options
- **GPT 3.5 Turbo**
- **GPT 3.5 Turbo (16K)***
- **GPT 4**

---


# Synthesizer

## Overview
LiaPlus AI supports multiple synthesizer providers to ensure high-quality voice synthesis for its AI voice assistants. This section outlines the supported synthesizer providers and their configuration options.

## Supported Synthesizer Providers

LiaPlus AI supports the following synthesizer providers:

- **Azure**
- **ElevenLabs**

## Azure Synthesizer

### Configuration Options
- **Model**
- **Language**

### Model Option 
-- **Azure Neural Voice**

### Language or Voice Options

#### **Afrikaans (South Africa) - af-ZA:**
- **Female:** af-ZA-AdriNeural3
- **Male:** af-ZA-WillemNeural3

#### **Arabic (United Arab Emirates) - ar-AE:**
- **Female:** ar-AE-FatimaNeural
- **Male:** ar-AE-HamdanNeural

#### **Bengali (India) - bn-IN:**
- **Female:** bn-IN-TanishaaNeural3
- **Male:** bn-IN-BashkarNeural3

#### **English (Australia) - en-AU:**
- **Female:** en-AU-NatashaNeural
- **Male:** en-AU-WilliamNeural

#### **English (United States) - en-US:**
- **Female:** en-US-AvaNeural, en-US-EmmaNeural, en-US-NovaMultilingualNeuralHD5
- **Male:** en-US-AndrewNeural, en-US-BrianNeural, en-US-OnyxMultilingualNeuralHD5

#### **Hindi (India) - hi-IN:**
- **Male:** hi-IN-AaravNeural
- **Female:** hi-IN-AnanyaNeural

## ElevenLabs Synthesizer

### Configuration Options
- **Model**
- **Voice**

### Model Options
- **Eleven Multilingual v2**

### Voice Options
- **Jeevan**

----

# Actions

## Overview
LiaPlus AI supports various actions to facilitate dynamic and flexible interactions within the AI voice assistants. This section outlines the supported actions and their respective configuration options and input schemas.

## Supported Actions

LiaPlus AI supports the following actions:

- **Send Mail**
- **Live Booking**
- **Call Transfer**
- **Data Extractor**
- **Create Custom Action**

## Send Mail Action

### Configuration Options
- **Name**
- **Description**
- **URL**

### Input Schema
The default input schema for the Send Mail action is:

```json
{
  "type": "object",
  "properties": {
    "caller_name": {
      "type": "string",
      "pattern": "^[A-Za-z0-9-]+$"
    },
    "caller_email_id": {
      "type": "string",
      "pattern": "^[+]?[0-9]{10,14}$"
    },
    "Details": {
      "type": "string",
      "pattern": "^[+]?[0-9]{10,14}$"
    }
  }
}
```

## Live Booking Action

### Configuration Options
- **Name**
- **Description**
- **URL**

### Input Schema
The default input schema for the Live Booking action is:

```json
{
  "type": "object",
  "properties": {
    "caller_name": {
      "type": "string",
      "pattern": "^[A-Za-z0-9-]+$"
    },
    "date_time": {
      "type": "string",
      "pattern": "^\\d{4}/\\d{2}/\\d{2} \\d{2}:\\d{2}$"
    },
    "Details": {
      "type": "string",
      "pattern": "^[+]?[0-9]{10,14}$"
    }
  }
}
```

## Call Transfer Action

### Configuration Options
- **Name**
- **Phone Number**

## Data Extractor Action

### Configuration Options
- **Name**
- **Description**
- **URL**

### Example Input Schema
An example input schema for the Data Extractor action is:

```json
{
  "type": "object",
  "properties": {
    "caller_name": {
      "type": "string",
      "pattern": "^[A-Za-z0-9-]+$"
    },
    "caller_email_id": {
      "type": "string",
      "pattern": "^[+]?[0-9]{10,14}$"
    },
    "caller_phone_no": {
      "type": "string",
      "pattern": "^[+]?[0-9]{10,14}$"
    }
  }
}
```

## Create Custom Action

### Configuration Options
- **Name**
- **Description**
- **URL**
- **Input Schema**

---- 

# Advanced Configuration

## Overview
LiaPlus AI provides advanced configuration options that give fine control over the interaction behavior and flow. This section outlines the available advanced configuration settings.

## Available Advanced Configuration Options

LiaPlus AI supports the following advanced configuration options:

- **Interruption Level**
- **Cutoff Flag**
- **Idle Time**
- **End Conversation on Goodbye**
- **Number of Human Checks**
- **Cut-off Response**

## Interruption Level

### Description
The **Interruption Level** setting defines the level of interruptions allowed during a conversation. 

### Values:
- **Low**: The assistant is less prone to interruptions.
- **High**: The assistant can be interrupted frequently.

## Cutoff Flag

### Description
The **Cutoff Flag** setting determines whether a human can interrupt the AI agent during a conversation.

### Values:
- **True**: The human can interrupt the AI agent at any time.
- **False**: The AI agent cannot be interrupted by the human.

## Idle Time

### Description
The **Idle Time** setting specifies the duration for which the AI assistant can remain idle before taking action.

## End Conversation on Goodbye

### Description
The **End Conversation on Goodbye** setting indicates whether the conversation should automatically terminate upon a goodbye message.

### Values:
- **True**: The call will end automatically when a goodbye is detected.
- **False**: The call will not end automatically on a goodbye.

## Number of Human Checks

### Description
The **Number of Human Checks** setting determines the duration the AI agent will wait for human input before taking action. If there is more than 15 seconds of silence during the call, the AI agent will resume speaking. The value set in this field specifies the maximum wait time for human interaction before the call is cut off.

## Cut-off Response

### Description
The **Cut-off Response** setting specifies a phrase that allows the caller to immediately interrupt the AI agent and regain control of the conversation.

----

# Conclusion
By offering support for a variety of transcriber ,LLM and synthesizer providers, LiaPlus AI ensures flexibility and adaptability for your transcription and language processing needs. Please refer to individual provider documentation for further customization options.



