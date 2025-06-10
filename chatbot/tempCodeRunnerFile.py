from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("api_key")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?