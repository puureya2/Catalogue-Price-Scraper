from Scrape import productInfo
from Scrape import searchURLs

import csv
import time


input_search = "iPhone"

# scrap search results & add data to url.txt
searchURLs()
time.sleep(5)

url_list = []

# fetch urls from url.txt
url_txt = open("url.txt", 'r')

for url in url_txt:
    url_list.append(url)

url_txt.close()


# add scrapped data to a dictionary
csv_dict = []
headings = ["No.", "Product", "Price", "Image", "WebPage"]

i = 1
for url in url_list:

    itemNumber = str(i)
    name = productInfo(url)['name']
    price = productInfo(url)['price']
    image = productInfo(url)['img']
    href = productInfo(url)['href']

    new_line = {}

    new_line.update({headings[0]: itemNumber})
    new_line.update({headings[1]: name})
    new_line.update({headings[2]: price})
    new_line.update({headings[3]: image})
    new_line.update({headings[4]: href})

    csv_dict.append(new_line)

    print("Data added [" + itemNumber + "]")
    i = i + 1

print("-> getData() Successful!")
time.sleep(5)


# add dictionary data to a new csv file
newFile_Name = "Satozim -" + input_search + "- Prices.csv"
newFile = r"Scraped Data\{}".format(newFile_Name)

tempFile = open(newFile, 'a')
tempFile.close()

with open(newFile, 'w', newline='') as csv_file:
    print("-> newFile: " + newFile_Name)

    writer = csv.DictWriter(csv_file, fieldnames=headings)
    writer.writeheader()

csv_file.close()

with open(newFile, 'a', newline='') as csv_file:
    print("-> newFile: " + newFile_Name)

    writer = csv.DictWriter(csv_file,
                            fieldnames=headings,
                            quoting=csv.QUOTE_NONE,
                            escapechar=',',
                            delimiter=',',
                            lineterminator=''
                            )

    writer.writerows(csv_dict)

csv_file.close()

print("-> Scrape Successful!")
