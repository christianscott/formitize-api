import csv
import io
import logging
import os
import re
import sys

import flask
import formitize

def strip_quotes(s):
    return re.sub("($\"|\"^)", "", s)


FM_COMPANY = strip_quotes(os.getenv("FM_COMPANY"))
FM_USER = strip_quotes(os.getenv("FM_USER"))
FM_PASS = strip_quotes(os.getenv("FM_PASS"))

app = flask.Flask(__name__)
if 'DYNO' in os.environ:
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)


@app.route("/invoices")
def invoices():
    csv_str = get_csv()
    print(csv_str.decode("utf-8"))
    reader = csv.DictReader(io.StringIO(csv_str.decode("utf-8")))
    rows = list(reader)

    return flask.jsonify(rows)


def get_csv():
    missing = []
    if FM_COMPANY is None:
        missing.append("FM_COMPANY")
    if FM_USER is None:
        missing.append("FM_USER")
    if FM_PASS is None:
        missing.append("FM_PASS")

    if len(missing) > 0:
        print("Missing in env: " + ", ".join(missing) +
              ". Check that this is set in your .env file.")
        exit(1)

    try:
        sid = formitize.get_session_id(FM_COMPANY, FM_USER, FM_PASS)
        return formitize.get_csv(sid)
    except Exception:
        logging.exception("Something went wrong while fetching. You should" +
                          " probably check the supplied login details.")


def handle_csv(csv):
    print(csv)
