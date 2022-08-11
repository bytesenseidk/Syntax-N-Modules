from datetime import date

def prettify_date():
    months = {"01":"January", "02":"February", "03":"March",
            "04":"April", "05":"May", "06":"June", "07":"July",
            "08":"August", "09":"September", "10":"October",
            "11":"November", "12":"December"}
            
    today = date.today().strftime("%d-%m-%Y").split("-")
    day, month, year = today[0], str(today[1]), today[2]
    return f"{day} {months[month]} {year}"

print(prettify_date())

