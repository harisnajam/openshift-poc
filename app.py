from flask import Flask
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now()

    return f"""
    <h1>Haris</h1>

    <p>Today's date is <b>{now.strftime('%Y-%m-%d')}</b></p>

    <p>The time now is <b>{now.strftime('%H:%M:%S')} GMT</b></p>

    <hr>

    <h3>OpenShift Information</h3>

    <ul>
        <li>Pod Name: {socket.gethostname()}</li>
        <li>Unix Timestamp: {int(now.timestamp())}</li>
        <li>Random Number: {now.microsecond}</li>
        <li>This page is running inside OpenShift.</li>
    </ul>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)