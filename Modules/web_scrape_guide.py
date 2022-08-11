# """ Web Scrape """

# import requests
# from bs4 import BeautifulSoup


# url = "https://www.google.com/search?q=bitcoin+price"

# def print_website_code(url):
#     source = requests.get(url).text
#     soup = BeautifulSoup(source, "html.parser")
#     # part = soup.find("div", attrs={"class": "dDoNo ikb4Bb gsrt gzfeS"}).find("div", 
#                             # attrs={"class": "DFlfde SwHCTb"}).text
#     part = soup.find("div", class_="dDoNo ikb4Bb gsrt gzfeS").text
#     return part
    


# # def print_website_part(url):
# #     source = requests.get(url).text
# #     soup = BeautifulSoup(source, "html.parser")
# #     print(soup.prettify())
# #     """ Find the class of the part you wish """
# #     part = soup.find("div", attrs={"class": "BNeawe s3v9rd AP7Wnd"}).find("div", 
# #                             attrs={"class": "BNeawe s3v9rd AP7Wnd"}).text
# #     print(part)

# # print_website_part(url)

# print(print_website_code(url))

# # <div class="dDoNo ikb4Bb gsrt gzfeS"><span class="DFlfde SwHCTb" data-precision="2" data-value="202091.4842">202.091,48</span> <span class="MWvIVe" data-mid="/m/01j9nc" data-name="Dansk krone">Dansk krone</span></div>

import requests 
import bs4 
  
# Taking thecity name as an input from the user
city = "Imphal"
  
# Generating the url  
url = "https://google.com/search?q=weather+in+" + city
  
# Sending HTTP request 
request_result = requests.get( url )
  
# Pulling HTTP data from internet 
soup = bs4.BeautifulSoup(request_result.text, "lxml" )
  
# Finding temperature in Celsius.
# The temperature is stored inside the class "BNeawe". 
temp = soup.find( "div" , class_='BNeawe' ).text 
    
print( temp ) 