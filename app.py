from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return "Webhook is live", 200
    else:
        data = request.json
        print(data)
        return "ok", 200
