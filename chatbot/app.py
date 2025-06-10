from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os
from dotenv import load_dotenv
import random

app = Flask(__name__)
load_dotenv()
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
    api_key= os.getenv("apikey")
    
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"reply": "Please send a valid message."})

    messages = [
        {"role": "user", "content": user_message}
    ]

    try:
        response = client.chat.completions.create(
            model="gemini-1.5-flash-latest",
            messages=messages
        )
        reply = random.choice(response.choices).message.content
    except Exception as e:
        reply = f"Sorry, something went wrong: {str(e)}"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
