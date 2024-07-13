import csv

# Shorten Product Names
stripped_names = []
file = r'Scraped Data\Satozim -iPhone- Prices.csv'


with open(file, 'r') as file_open:

    heading = next(file_open)
    csv = csv.reader(file_open)

    for row in csv:
        stripped_name = row[1].replace('Apple ', '').strip()
        stripped_names.append(stripped_name)

file_open.close()

print(stripped_names)
