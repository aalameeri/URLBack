from flask import Flask

app = Flask(__name__)

@app.route("/callback")
def hello():
    return "Hello, World!"