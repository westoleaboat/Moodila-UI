from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/moods')
def get():
    return requests.get('https://moodila.onrender.com').content