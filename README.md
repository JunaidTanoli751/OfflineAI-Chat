# OfflineAI-Chat
# LocalAI-Chat 🤖

A **local AI chatbot** built with **Streamlit** and **Ollama Phi-3 Mini**.  
Chat with AI **without internet or external APIs** — everything runs locally on your machine!

---

## Features

- Local AI chatbot (no API calls, no internet required)
- Uses **Ollama Phi-3 Mini 128k model**
- Interactive UI using **Streamlit**
- Maintains **chat history** in the session
- Easy to run on your local machine

---

## Project Structure

LocalAI-Chat/
│
├─ app.py # Main Streamlit app
├─ requirements.txt # Dependencies
├─ .gitignore # Files to ignore (env, cache, etc.)
└─ README.md # Project documentation

How It Works

User types a message in the Streamlit chat input.

The message is sent to Ollama Phi-3 Mini for local processing.

AI response is displayed in the chat interface.

Chat history is stored in the session.

Tech Stack

Python

Streamlit for UI

Ollama Phi-3 Mini for local AI inference











