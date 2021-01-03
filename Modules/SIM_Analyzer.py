import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate

def number_scanner(phone_number):
    number = phonenumbers.parse(phone_number)
    description = geocoder.description_for_number(number, "en")
    supplier = carrier.name_for_number(number, "en")
    info = [["Country", "Supplier"],
            [description, supplier]]
    data = str(tabulate(info, headers="firstrow", tablefmt="github"))
    return data

if __name__ == "__main__":
    number = input("Enter Number: ")
    print(number_scanner(number))

