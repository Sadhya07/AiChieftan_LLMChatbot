import os
import requests
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

def generate_response(message):
    lower_msg = message.lower()

    # FAQ shortcuts
    faq_answers = {
        "check in time": "Check-in starts at 2 PM.",
        "check out time": "Check-out is before 11 AM.",
        "breakfast": "Breakfast is served from 6:30 AM to 10:30 AM daily.",
        "wifi": "Free WiFi is available throughout the hotel with network 'HotelGuest' and password 'Welcome123'."
    }

    for question, answer in faq_answers.items():
        if question in lower_msg:
            return answer

    # Fallback to Groq API
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful hotel concierge."},
            {"role": "user", "content": message}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content']
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

# Streamlit UI
st.title("Hotel Concierge Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        response = generate_response(prompt)
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    
    
    


    
    