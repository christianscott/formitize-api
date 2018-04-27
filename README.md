# Keboola Formitize CSV fetching extension

> Maintained by [Christian Scott](me@christianfscott.com)

REST API for interfacing with Keboola Generic Extension.

## Configuration

```
params = {
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
```

## Running locally

To run this, you'll need `Python 3.6` (or greater) and `pipenv` installed. Example workflow below:

```shell
$ pipenv install
...

$ pipenv shell
...

(pipenv-shell) $ heroku local # or gunicorn app:app --logging-file=-
```

`Pipenv` automatically installs dependencies and the correct version of the Python interpreter.

This should "just work" on Windows, but if it doesn't, try `pip` instead:

```
$ pip install -r requirements.txt
$ python main.py
```

Make sure that pip & python both point to the Python 3.6 (or greater) version.

## Deployment

Pushing to Heroku is as simple as this:

```
$ git add .
$ git commit -m "<description>"
$ git push heroku master
```

You'll need to be signed in to heroku for this.

## Documentation

- https://docs.python.org/3/using/windows.html
- https://docs.pipenv.org/
- https://developers.keboola.com/extend/generic-extractor/
