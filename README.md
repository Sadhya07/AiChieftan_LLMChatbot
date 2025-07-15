# AiChieftan_LLMChatbot


AIChieftan is a full-stack, LLM-powered chatbot web application designed for seamless user interaction, real-time response generation, and insightful analytics — all in one package. It includes a backend API, frontend UI, Streamlit dashboard for monitoring, and QR code integration for easy access and sharing.

---

## Features

- **Conversational Chatbot** using OpenAI API
- **Frontend Interface** built with HTML/CSS/JS
- **Python Flask Backend** to handle requests and responses
- **Streamlit Dashboard** for real-time visualization of usage and performance
- **QR Code Generator** to quickly access or share the chatbot
- **Environment Variable Management** for secure API key usage

---

## Project Structure

```bash
AIChieftan/
├── backend/
│   ├── app.py               # Flask server
│   ├── chat.py              # Handles chatbot logic
│   └── templates/
│       └── index.html       # Web UI
├── frontend/
│   ├── index.html           # Static frontend
│   └── script.js            # JS logic for interaction
├── dashboard/
│   └── streamlit_app.py     # Analytics dashboard
├── qr_code/
│   └── generate_qr.py       # QR code generation script
├── .env                     # API keys and sensitive configs
├── .gitignore
├── requirements.txt
└── README.md




#Note
Some of the code has been referenced from third party apps and is AI generated.