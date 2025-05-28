from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/2007494042/callback", methods=["POST"])
def callback():
    print("Webhook received!")
    return jsonify({"status": "ok"}), 200
