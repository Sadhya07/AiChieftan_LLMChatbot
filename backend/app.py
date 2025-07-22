from flask import Flask, request, jsonify
from flask_cors import CORS
from chat import get_ai_reply
import os

app = Flask(__name__)

# Enable CORS for all domains and headers
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"reply": "No input provided"}), 400

    ai_response = get_ai_reply(user_message)
    return jsonify({"reply": ai_response})


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)  # Important for Render
