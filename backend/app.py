from flask import Flask, request, jsonify
from flask_cors import CORS
from chat import get_ai_reply

app = Flask(__name__)
CORS(app)  # Allow requests from frontend or Streamlit

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"reply": "No input provided"}), 400

    ai_response = get_ai_reply(user_message)
    return jsonify({"reply": ai_response})

if __name__ == "__main__":
    app.run(debug=True)
