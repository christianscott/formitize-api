import enum
import json
import re

import flask

options = {
    "date": {
        "paydate": { "title": "Date Paid" },
        "expectedpaydate": { "title": "Expected Pay Date" },
        "invoicedate": { "title": "Invoice Date" },
        "dateCreated": { "title": "Date Created" },
        "dateModified": { "title": "Last Modified" }
    },
    "select": {
        "paid": { 
            "options": {"all": "", "paid": "2", "unpaid": "1", "overdue": "3"},
            "title": "Payment Status"
        },
        "paysource": {
            "options": {
                "All Methods": "-2",
                "Cash": "CASH",
                "EFT": "EFT",
                "Cheque": "CHEQUE",
                "Card": "CARDRECORD"
            },
            "title": "Payment Method"
        },
        "status": {
            "options": {
                "All Status": "-2",
                "Draft": "0",
                "Open": "1",
                "Cancelled": "3"
            },
            "title": "Status"
        },
        "hasexternalsourceid": {
            "options": { "Any": "-2", "No": "0", "Yes": "1" },
            "title": "Is In Accounting"
        },
        "hasduplicatepaymentamount": {
            "options": { "Any": "-2", "No": "0", "Yes": "1" },
            "title": "Has Duplicate Payment Amount"
        },
        "overpaid": {
            "options": { "Any": "-2", "No": "0", "Yes": "1" },
            "title": "Overpaid"
        }
    },
    "search": {
        "invoicenumber": { "title": "Invoice Number" },
        "reference": { "title": "Reference" },
        "title": { "title": "Title" },
        "summary": { "title": "Summary" },
        "terms": { "title": "Terms" }
    },
    "number": {
        "subtotal": { "title": "Sub Total" },
        "tax": { "title": "Tax Amount" },
        "total": { "title": "Total" },
        "paid": { "title": "Amount Paid" }
    }
}


class Paid(enum.Enum):
    ALL = 0
    PAID = 1
    UNPAID = 2
    OVERDUE = 3


class InvoiceFilters:
    def __init__(self, options):
        self.options = options
        self.__data = {}
    
    @staticmethod
    def from_request(req: flask.request) -> "InvoiceFilters":
        filters = InvoiceFilters(options)

        for key in filters.options["search"]:
            seach_term = req.args.get("search." + key, default=None)
            if seach_term is not None:
                filters.add_search(key, seach_term)

        for key in filters.options["select"]:
            selected = req.args.get("select." + key, default=None)
            if selected is not None and selected in filters.options["select"][key]["options"]:
                encoded = filters.options["select"][key]["options"][selected]
                filters.add_select(key, encoded)

        for key in filters.options["date"]:
            date = req.args.get("date." + key, default=None)
            if date is not None:
                frm, to, *_ = date.split(",")
                filters.add_date(key, frm, to)

        for key in filters.options["number"]:
            num = req.args.get("number." + key, default=None)
            if num is not None:
                frm, to, *_ = num.split(",")
                filters.add_number(key, frm, to)
        
        return filters
    
    def to_dict(self):
        if "paid" not in self.__data:
            self.add_paid("overdue")
        
        return self.__data

    def add_paid(self, paid: str):
        self.__add("paid", paid)
    
    def add_date(self, name, frm, to):
        if frm != "":
            self.__add(name + "-from", frm)
        if to != "":
            self.__add(name + "-to", to)
    
    def add_select(self, name, selected):
        self.__add(name, selected)

    def add_search(self, name, s):
        self.__add(name, s)

    def add_number(self, name, frm, to):
        self.__add(name + "-toNum", format_number(to))
        self.__add(name + "-fromNum", format_number(frm))

    def __add(self, key, value):
        # all filter values are wrapped in an array
        self.__data[key] = [value]


def format_date(date):
    if date is None:
        return ""

    return date.strftime("%d %B %Y")


def format_number(num):
    if num is None:
        return ""
    
    return str(num)
