from flask import jsonify, Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"
    
    