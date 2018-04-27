import datetime
import enum
import json

import requests

import formitize.invoice as invoice

ROOT_URL = "https://service.formitize.com.au"
ACCOUNTS_URL = ROOT_URL + "/crm/reports"


def get_session_id(company, username, password):
    # POST creds to the root to get the session id

    data = {"global": "true",
            "post": "login",
            "type": "user",
            "company": company,
            "username": username,
            "password": password}
    r = requests.post(ROOT_URL, data=data)

    if len(r.history) < 1:
        raise Exception("Bad request: {} redirects happened, expected at least 1".format(len(r.history)))

    sid = r.history[0].cookies['sid']
    if sid is None or sid == "":
        return Exception("sid should be a non-empty string, got {} instead".format(sid))

    return sid


# TODO: support other options including "deleted": "1" etc
def get_csv(session_id, search=""):
    # using the session id from before, download the accounts csv with options

    filters = invoice.InvoiceFilters()
    filters.add_paid(invoice.Paid.UNPAID)

    data = filters.to_dict()

    data = {"post": "invoices",
            "type": "crm/downloadcsv",
            "global": "true",
            "value": search,
            "data": data}
    cookies = {"sid": session_id}
    r = requests.post(ACCOUNTS_URL, data=data, cookies=cookies)

    if r.status_code != 200:
        raise Exception("accounts response not ok")

    return r.content
