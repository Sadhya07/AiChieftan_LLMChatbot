import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"  # or llama3, gemma, etc.

def generate_response(message):
    lower_msg = message.lower()
    
    # Your FAQ shortcut
    faq_answers = {
        "check in time": "Check-in starts at 2 PM.",
        "check out time": "Check-out is before 11 AM.",
        
    }

    for question, answer in faq_answers.items():
        if question in lower_msg:
            return answer

    # Fallback to Groq
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
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    return data['choices'][0]['message']['content']
