from flask import Flask

api = Flask(__name__)

@api.route("/encode")
def encode():
    return "Encoded"

@api.route("/decode")
def decode():
    return "Decoded"
