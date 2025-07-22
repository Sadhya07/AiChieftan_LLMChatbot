import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

# Predefined FAQ-like answers for common hotel-related questions
faq_answers = {
    "check in": "Check-in time starts at 2:00 PM. Early check-in may be available upon request.",
    "check out": "Check-out is before 11:00 AM. You can request late checkout at the front desk.",
    "wifi": "Free WiFi is available throughout the hotel. Network: 'HotelGuest', Password: 'Welcome123'.",
    "breakfast": "Breakfast is served in the dining hall from 6:30 AM to 10:30 AM every day.",
    "parking": "Yes, we offer complimentary valet parking for all guests.",
    "spa": "The hotel spa is open daily from 9 AM to 9 PM. Advance booking is recommended.",
    "pool": "The swimming pool is open from 7 AM to 8 PM. Towels are available poolside.",
    "room service": "Room service is available 24/7. Dial 9 from your room phone to order.",
    "laundry": "Laundry services are available. Please use the laundry bag and form provided in your room."
}

# Clean response text if needed
def clean_response(text):
    return text.strip().replace("\n\n", "\n")

# Main function to generate AI reply
def get_ai_reply(message: str) -> str:
    message = message.lower()

    # Check if question matches FAQs
    for keyword, answer in faq_answers.items():
        if keyword in message:
            return answer

    # If not in FAQ, call Groq API
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": GROQ_MODEL,
            "messages": [
                {"role": "system", "content": "You are a polite and efficient AI concierge at a luxury hotel. Assist the guest with hospitality-related queries."},
                {"role": "user", "content": message}
            ]
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        ai_reply = data["choices"][0]["message"]["content"]
        return clean_response(ai_reply)

    except Exception as e:
        return f"Sorry, something went wrong while processing your request: {str(e)}"
