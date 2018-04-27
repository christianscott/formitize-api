import flask
import logging
import os
import sys

app = flask.Flask(__name__)
if 'DYNO' in os.environ:
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)

@app.route("/invoices")
def invoices():
    count = flask.request.args.get("count", default=1, type=int)
    pairs = [{ "key": "val" }] * count
    return flask.jsonify({ "pairs": pairs })

