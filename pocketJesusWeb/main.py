import requests
from bs4 import BeautifulSoup
import csv

bible_api_url = "https://bible-api.com/romans+12:1-2"

jesus_quotes_url = "https://www.eldoradoweather.com/current/jesus-quotes.php"

# Make a request to the website
jesus_response = requests.get(jesus_quotes_url)

# Parse the HTML data
soup = BeautifulSoup(jesus_response.text, 'html.parser')

td_elements = soup.find_all('td')

quotes = []
for quote in soup.find_all('b'):
    quotes.append(quote.text)


response = requests.get(bible_api_url)
print(response.text)
