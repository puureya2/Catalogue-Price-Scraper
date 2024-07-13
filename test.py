
newFile_Name = "Satozim -" + "iPhone" + "- Prices.csv"
newFile = "Scraped Data\{}".format(newFile_Name)

print("-> newFile Directory: " + newFile)

tempFile = open(newFile, 'a')
tempFile.close()

with open(newFile, 'w') as csv_file:
    print("-> newFile: " + newFile_Name)
    csv_file.write("WORKED")
    csv_file.close()

