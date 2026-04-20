from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Server OK"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("DATA:", data)
    return "ok"