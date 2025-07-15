from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.chat import generate_response
import json

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = generate_response(user_input)
    return jsonify({"response": response})

@app.route("/")
def index():
    return "Hospitality Chatbot API Running"

if __name__ == "__main__":
    app.run(debug=True)