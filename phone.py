import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

def number_check(phone_number):
    info = []
    number = phonenumbers.parse(phone_number)
    info.append(geocoder.description_for_number(number, "en"))
    info.append(carrier.name_for_number(number, "en"))
    return info

if __name__ == "__main__":
    number = input("Enter number: ")
    print(number_check(number))


