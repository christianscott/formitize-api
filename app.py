import flask
import logging
import os
import re

import formitize

app = flask.Flask(__name__)

@app.route("/invoices")
def invoices():
    count = flask.request.args.get("count", default=1, type=int)
    pairs = [{ "key": "val" }] * count
    return flask.jsonify({ "pairs": pairs })

