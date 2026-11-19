# 🛡️ CyberSec AI Chatbot

A Python-based AI chatbot designed to act as a Blue Team Security Assistant. It uses the Groq API to generate cybersecurity-related responses and demonstrates basic LLM integration, prompt engineering, conversation history, and token management.

## 🎯 Project Overview
The chatbot is designed to assist users with cybersecurity topics through a predefined system prompt and an interactive conversation.

## ✨ Features

- **LLM Integration:** Connects to an LLM through the Groq API.
- **Custom System Prompt:** Defines the assistant's role and behavior as a Blue Team Security Assistant.
- **Conversation History:** Maintains previous user and assistant messages during the session.
- **Token Counting:** Uses Tiktoken to estimate the number of tokens in conversation messages.
- **Token Budget Management:** Removes older conversation messages when the configured token budget is exceeded.
- **Interactive CLI:** Allows users to communicate with the chatbot through the terminal.

## 🛠️ Technologies

- Python 3
- Groq API
- OpenAI Python SDK
- Tiktoken

## 📋 Prerequisites

Before running the project, make sure you have:

- Python 3.9 or later.
- A Groq API key.
- Internet access.

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/djeroufouzia/cybersec-ai-chatbot.git
```

**2. Navigate to the project directory**

```bash
cd cybersec-ai-chatbot
```

**3. Install dependencies**

```bash
pip install openai tiktoken
```

## 🔐 Environment Configuration

The chatbot requires a Groq API key to communicate with the LLM.

**1. Get your API key**

Create an account at [Groq Console](https://console.groq.com/) and generate an API key.

**2. Set the environment variable**

On macOS or Linux, open your terminal and run:

```bash
export GROQ_API_KEY="your_actual_api_key"
```

Replace `your_actual_api_key` with your real API key.

**3. Verify the environment variable**

```bash
echo $GROQ_API_KEY
```

Make sure the variable is configured before running the application.

## ▶️ Usage

Run the chatbot:

```bash
python3 chatbot.py
```

Start asking cybersecurity questions.

To exit the chatbot, type:

```text
exit
```

or

```text
quit
```

## 🧠 Concepts Practiced

This project demonstrates practical use of:

- Large Language Models (LLMs)
- API integration
- Prompt Engineering
- System and User Messages
- Conversation History
- Tokenization
- Context and Token Budget Management


## 📌 Project Status

Beginner project – Work in Progress.

This project is part of my practical learning journey in Artificial Intelligence and Cybersecurity.

## 👩‍💻 Author

**Fouzia Djerou**

GitHub: [@djeroufouzia](https://github.com/djeroufouzia)
