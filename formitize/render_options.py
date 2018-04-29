def render(opts) -> str:
    out = "<form>"
    
    out += '<div class="bg-silver"><h2>Dates</h2>'
    for key in opts["date"]:
        out += render_date("date." + key, opts["date"][key])
    out += "</div>"

    out += '<div class="bg-silver"><h2>Numbers</h2>'
    for key in opts["number"]:
        out += render_number("number." + key, opts["number"][key])
    out += "</div>" 

    out += '<div class="bg-silver"><h2>Selects</h2>'
    for key in opts["select"]:
        out += render_select("select." + key, opts["select"][key])
    out += "</div>" 

    out += '<div class="bg-silver"><h2>Search</h2>'
    for key in opts["search"]:
        out += render_search("search." + key, opts["search"][key])
    out += "</div>" 

    out += '<input type="submit" value="Get the config">'
    out += "</form>"

    return out


def render_select(key: str, opts) -> str:
    title = opts["title"]

    out = f'<label for="{key}" class="mr1">{title}</label>'
    out += f'<select name="{key}"><option disabled selected value>'

    for value in opts["options"]:
        out += f'<option value="{value}">{value}</option>'

    out += '</select>'

    return out


def render_search(key: str, opts) -> str:
    title = opts["title"]

    out = render_input(key, title)

    return f'<div class="mb2">{out}</div>' 


def render_number(key: str, opts) -> str:
    title = opts["title"]

    out = f'<h4 class="m0">{title}</h4>'
    out += render_input(key + "-from", "from", "number")
    out += render_input(key + "-to", "to", "number")

    return f'<div class="mb2">{out}</div>'


def render_date(key: str, date) -> str:
    title = date["title"]

    out = f'<h4 class="m0">{title}</h4>'
    out += render_input(key + "-from", "from", "date")
    out += render_input(key + "-to", "to", "date")

    return f'<div class="mb2">{out}</div>'


def render_input(name: str, label: str = "", input_type: str = "text") -> str:
    out = f'<label for="{name}" class="mr1">{label}</label>'
    out += f'<input type="{input_type}" name="{name}" id="{name}" placeholder="{label}" class="rounded border">'
    return out
