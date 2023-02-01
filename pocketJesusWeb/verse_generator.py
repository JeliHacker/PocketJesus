import requests
import csv
# import pandas as pd

# there are 2040 Jesus verses total

bible_api_url = "https://bible-api.com/"

params = {
    "translation": "bbe"
}

url = "https://bible-api.com/matthew3:15"

with open('verses_numbered.csv', 'r', encoding='utf-8') as input_file:
    # Create a CSV reader object
    reader = csv.reader(input_file)

    with open('quotes_expanded_with_verses.csv', 'a', encoding='utf-8') as output_file:
        writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC)

        count = 0
        for row in reader:

            if count == 0:
                print("Do nothing")

            elif 201 <= int(row[0]) <= 250:
                verse = row[1].replace(" ", "").lower()

                url = bible_api_url + verse

                response = requests.get(url=url)

                row.append(response.json()["text"])

                writer.writerow(row)

            count += 1
