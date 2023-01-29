import requests
from bs4 import BeautifulSoup
import csv

jesus_quotes_url = "https://www.eldoradoweather.com/current/jesus-quotes.php"

# Open the input CSV file
with open('quotes_perfect.csv', 'r') as input_file:
    # Create a CSV reader object
    reader = csv.reader(input_file)

    # Open the output CSV file
    with open('quotes_expanded.csv', 'w') as output_file:
        # Create a CSV writer object
        writer = csv.writer(output_file)

        # Iterate through the rows
        for row in reader:

            # Get the "Quote" value
            quote = row[0]
            # print(quote.split('-'))

            if '-' in quote:
                # Split the quote into a start and end value
                start, end = quote.split('-')[0], quote.split('-')[1]
                start_book, start_verse = start.split(' ')

                chapter_num = start_verse.split(':')[0]
                start_verse = start_verse.split(':')[1]
                end_verse = end.split(':')[1]

                for num in range(int(start_verse), int(end_verse) + 1):
                    row = [f"{start_book} {str(chapter_num)}:{str(num)}"]

                    writer.writerow(row)

            elif 'to' in quote:
                start, end = quote.split('to')[0], quote.split('to')[1]

                book = start.split(' ')[0]
                chapter = start.split(' ')[1].split(':')[0]

                start_verse = start.split(' ')[1].split(':')[1]
                end_verse = end.split(':')[1]

                for num in range(int(start_verse), int(end_verse)+1):
                    row = [f"{book} {chapter}:{num}"]
                    print(row)
                    writer.writerow(row)

            else:
                # Write the original row to the output CSV file
                writer.writerow(row)