import datetime
import enum

def date_option(date: datetime.date = None) -> str:
    if date is None:
        return ""
    
    return date.strftime("%d %B %Y")

class Paid(enum.Enum):
    ALL = 0
    PAID = 1
    UNPAID = 2
    OVERDUE = 3

def paid_option(paid):
    if paid == Paid.ALL:
        return ""

    if paid == Paid.PAID:
        return "2"

    if paid == Paid.UNPAID:
        return "1"

    if paid == Paid.OVERDUE:
        return "3"

    raise TypeError("could not get paid code for " + str(paid))

class InvoiceRequest:
    def __init__(self):
        pass