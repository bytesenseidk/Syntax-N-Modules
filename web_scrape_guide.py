""" Web Scrape """

import requests
from bs4 import BeautifulSoup


url = "https://www.google.com/"

def print_website_code(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")
    print(soup.prettify())


def print_website_part(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")
    print(soup.prettify())
    """ Find the class of the part you wish """
    part = soup.find("div", attrs={"class": "BNeawe s3v9rd AP7Wnd"}).find("div", 
                            attrs={"class": "BNeawe s3v9rd AP7Wnd"}).text
    print(part)

print_website_part(url)