import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

faq_answers = {
    "check in time": "Check-in starts at 2 PM.",
    "check out time": "Check-out is before 11 AM.",
    "restaurant": "The hotel restaurant is open from 7 AM to 10 PM.",
    "gym": "The gym is open 24/7 for all guests."
}

def generate_response(message):
    lower_msg = message.lower()
    for question, answer in faq_answers.items():
        if question in lower_msg:
            return answer

    # Fallback to OpenAI GPT if no predefined answer found
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful hotel concierge."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message["content"].strip()