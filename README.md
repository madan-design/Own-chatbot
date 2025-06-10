# Own-chatbot
# 🧠 Flask Chatbot with Gemini API

This is a simple web-based chatbot application built using **Flask** and **Google's Gemini API** (accessed through OpenAI's client format). It uses a front-end form to accept user input, sends it to the backend, and returns an AI-generated response.

## 🚀 Features

- Simple Flask backend
- Gemini 1.5 model integration
- Randomized response selection (if multiple choices exist)
- `.env` support for API key security
- Frontend via `index.html`

## 📁 Project Structure

├── app.py
├── templates/
│ └── index.html
├── .env
├── requirements.txt
└── README.md


## 🧑‍💻 Getting Started

1. Clone the Repository

git clone https://github.com/yourusername/flask-gemini-chatbot.git
cd flask-gemini-chatbot

2. Install Dependencies
Use pip to install the required Python packages:

bash
Copy
Edit
pip install -r requirements.txt

3. Setup Environment Variables
Create a .env file in the root directory and add your Gemini API key:

apikey=YOUR_GEMINI_API_KEY

4. Run the Flask App
python app.py
The app will be running on: http://localhost:5000

How It Works
User inputs a message on the frontend.

JavaScript sends the message as JSON to the /chat endpoint.

The Flask app sends it to Gemini using the OpenAI-compatible format.

Gemini responds with generated text.

The Flask app sends it back to the frontend for display.

