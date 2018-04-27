import enum
import json

options = {
    "date": {
        "paydate": { "title": "Date Paid" },
        "expectedpaydate": { "title": "Expected Pay Date" },
        "invoicedate": { "title": "Invoice Date" },
        "dateCreated": { "title": "Date Created" },
        "dateModified": { "title": "Last Modified" }
    },
    "select": {
        "paysource": {
            "options": {
                "-2": "All Methods",
                "CASH": "Cash",
                "EFT": "EFT",
                "CHEQUE": "Cheque",
                "CARDRECORD": "Card"
            },
            "title": "Payment Method"
        },
        "status": {
            "options": {
                "-2": "All Status",
                "0": "Draft",
                "1": "Open",
                "3": "Cancelled"
            },
            "title": "Status"
        },
        "hasexternalsourceid": {
            "options": { "-2": "Any", "0": "No", "1": "Yes" },
            "title": "Is In Accounting"
        },
        "hasduplicatepaymentamount": {
            "options": { "-2": "Any", "0": "No", "1": "Yes" },
            "title": "Has Duplicate Payment Amount"
        },
        "overpaid": {
            "options": { "-2": "Any", "0": "No", "1": "Yes" },
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
    def __init__(self):
        self.__data = {}
    
    @staticmethod
    def from_json(json):
        pass
    
    def to_dict(self):
        if "paid" not in self.__data:
            self.add_paid(Paid.ALL)
        
        return self.__data

    def add_paid(self, paid):
        self.__add("paid", paid)
    
    def add_date(self, name, to=None, frm=None):
        assert name in options["date"], \
            "name '{}' missing in options['date']".format(name)

        self.__add(name + "-to", format_date(to))
        self.__add(name + "-from", format_date(frm))
    
    def add_select(self, name, selected):
        assert name in options["select"], \
            "name '{}' missing in options['select']".format(name)
        assert selected in options["select"][name], \
            "option '{}' missing in options['select']['{}']".format(selected, name)
    
    def add_search(self, name, s):
        assert name in options["search"], \
            "name '{}' missing in options['search']".format(name)

        self.__add(name, s)

    def add_number(self, name, to=None, frm=None):
        assert name in options["number"], \
            "name '{}' missing in options['number']".format(name)

        self.__add(name + "-toNum", format_number(to))
        self.__add(name + "-fromNum", format_number(frm))

    def __add(self, key, value):
        # all filter values are wrapped in an array
        self.__data[key] = [value]


def format_paid(paid):
    if paid == Paid.ALL:
        return ""

    if paid == Paid.PAID:
        return "2"

    if paid == Paid.UNPAID:
        return "1"

    if paid == Paid.OVERDUE:
        return "3"

    raise TypeError("could not get paid code for " + str(paid))


def format_date(date):
    if date is None:
        return ""

    return date.strftime("%d %B %Y")


def format_number(num):
    if num is None:
        return ""
    
    return str(num)
