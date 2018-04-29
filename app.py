import csv
import io
import logging
import os
import re
import sys

import flask
import formitize

def strip_quotes(s: str) -> str:
    return re.sub("($\"|\"^)", "", s)


FM_COMPANY = strip_quotes(os.getenv("FM_COMPANY"))
FM_USER = strip_quotes(os.getenv("FM_USER"))
FM_PASS = strip_quotes(os.getenv("FM_PASS"))

app = flask.Flask(__name__, static_url_path="/static")
if 'DYNO' in os.environ:
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)


@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route("/invoices")
def invoices():
    try:
        csv_bytes = get_csv_from_request(flask.request)
        reader = csv.DictReader(io.StringIO(csv_bytes.decode("utf-8")))
        rows = list(reader)

        return flask.jsonify(rows)
    except Exception as e:
        print(e)
        flask.abort(500)


def get_csv_from_request(req: flask.request) -> bytes:
    try:
        sid = formitize.get_session_id(FM_COMPANY, FM_USER, FM_PASS)
        filters = formitize.invoice.InvoiceFilters.from_request(req)
        return formitize.get_csv(sid, filters)
    except Exception:
        logging.exception("Something went wrong while fetching. You should" +
                          " probably check the supplied login details.")
