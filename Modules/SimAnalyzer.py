import os
import json
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate
from urllib.request import urlopen

class NumberAnalyzer(object):
    def __init__(self, number):
        self.number = phonenumbers.parse(number)
        self.url = "https://ipinfo.io/"

    def analyze(self):
        description = geocoder.description_for_number(self.number, "en")
        supplier = carrier.name_for_number(self.number, "en")
        response = urlopen(self.url)
        data = json.load(response)
        return [description, supplier, data]
    
    @property
    def parse_data(self):
        country, supplier, device = self.analyze()
        region = device["region"]
        city = device["city"]
        lat, lon = str(device["loc"]).split(",")
        location = f"Latitude: {lat}, Longtitude: {lon}"
        postal = device["postal"]
        timezone = device["timezone"]
        server = device["org"]
        hostname = device["hostname"]
        ip = device["ip"]
        return [["Country", country], ["Region", region], ["City", city], ["Location", location], 
                ["Postal", postal], ["Timezone", timezone], ["Server", server], ["Hostname", hostname], 
                ["Supplier", supplier], ["IP", ip]]
    
    def __str__(self):
        return str(f"\n{tabulate(self.parse_data)}")

if __name__ == "__main__":
    os.system("cls")
    print("[ Simcard Analyzer - python_genius ]\n")
    number = input("Enter Number: ")
    analyze = NumberAnalyzer(number)
    print(analyze)
    