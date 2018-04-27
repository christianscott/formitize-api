from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/values")
def hello():
    return jsonify({ "pairs": [{ "key": "val" }] })

