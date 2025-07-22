# AiChieftan_LLMChatbot


AIChieftan is a full-stack, LLM-powered chatbot web application designed for seamless user interaction, real-time response generation, and insightful analytics — all in one package. It includes a backend API, frontend UI, Streamlit dashboard for monitoring, and QR code integration for easy access and sharing.

---

## Features

- **Conversational Chatbot** using Groq API
- **Frontend Interface** built with Streamlit having CSS/HTML
- **Python Flask Backend** to handle requests and responses
- **Streamlit Dashboard** for real-time visualization of usage and performance
- **QR Code Generator** to quickly access or share the chatbot
- **Environment Variable Management** for secure API key usage

---

## Project Structure

```bash
AIChieftan/
├── assets/
│   └── icon.png                     # Icon used in Streamlit
├── backend/
│   ├── app.py                       # Flask server
│   ├── chat.py                      # Handles LLM responses
│   ├── requirements.txt             # Backend dependencies
│   └── test.py                      # Testing script
├── frontend/
│   ├── streamlit_app.py             # Streamlit dashboard
│   └── requirements.txt             # Streamlit dependencies
├── qr_code/
│   ├── generate_qr.py               # QR generator script
│   └── hotel_chatbot_qr.png         # Generated QR image
├── .env                             # Contains API keys (not committed)
├── .gitignore
└── README.md

##Pitch Desk

**Demo Video**: [Watch here](https://drive.google.com/file/d/1xerCs8gBxGaXvtrUuS7wJ4dFN1EFGU6g/view?usp=drive_link)

**PPT **: [View here](https://drive.google.com/file/d/1vNst2DzoC-zV3PRaFxdvi-Q-irMTBReP/view?usp=sharing)

**Deplyment Link**: (https://aichieftanllmchatbot-hospitality.streamlit.app/)

**QR Code** :(https://drive.google.com/file/d/1_zkNU7sTzivGAMP2FLrj6gMn8-ozIP0f/view?usp=drive_link)


#Note
Some of the code has been referenced from third party apps and is AI generated.