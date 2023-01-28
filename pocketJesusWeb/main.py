import requests
from bs4 import BeautifulSoup
import csv

bible_api_url = "https://bible-api.com/genesis3:16"

jesus_quotes_url = "https://www.eldoradoweather.com/current/jesus-quotes.php"

# Make a request to the website
jesus_response = requests.get(jesus_quotes_url)

# Parse the HTML data
soup = BeautifulSoup(jesus_response.text, 'html.parser')

td_elements = soup.find_all('td')

quotes = []
for quote in soup.find_all('b'):
    quotes.append(quote.text)


# Write the quotes to a CSV file
# with open('quotes.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Quote'])
#     for quote in quotes:
#         writer.writerow([quote])

# Open the input CSV file
with open('quotes_edited.csv', 'r') as input_file:
    # Create a CSV reader object
    reader = csv.reader(input_file)

    # Open the output CSV file
    with open('quotes_perfect.csv', 'w') as output_file:
        # Create a CSV writer object
        writer = csv.writer(output_file)

        # Iterate through the rows
        matthew_found = False
        for row in reader:
            # Check if the value of the "Quote" column starts with "Matthew"
            print(row, row[0])
            row[0] = row[0][:-1]

            writer.writerow(row)


