from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


PATH = r"C:\Program Files (x86)\chromedriver.exe"
cService = webdriver.ChromeService(executable_path=PATH)
driver = webdriver.Chrome(service=cService)


def searchURLs():

    driver.get("https://www.satozim.co.zw/")
    time.sleep(10)

    search = driver.find_element(By.NAME, "search")
    search.send_keys("iPhone")
    time.sleep(5)
    search.send_keys(Keys.RETURN)
    time.sleep(10)

    list_urls = []

    result = requests.get(driver.current_url)
    web_page = BeautifulSoup(result.text, "html.parser")
    time.sleep(10)

    item_classAtt = {"class": "block shadow-md bg-white border border-neutral-200 rounded-lg overflow-hidden"}
    doc_findItemTags = web_page.find_all("a", item_classAtt)

    url_txt = open("url.txt", 'w')
    url_index = 1

    for tag in doc_findItemTags:

        doc_findItemTag_attURL = tag["href"]
        add_url = "https://www.satozim.co.zw" + doc_findItemTag_attURL + "\n"
        url_txt.write(add_url)

        print("Url added [" + str(url_index) + "]")
        url_index = url_index + 1


    url_txt.close()

    time.sleep(10)
    driver.quit()

    print("-> getURLs() Successful!")

    return list_urls


def productInfo(url):

    result = requests.get(url)
    web_page = BeautifulSoup(result.text, "html.parser")

    doc_withoutBS4 = result.text
    doc_raw = web_page
    doc_pretty = web_page.prettify()

    doc_findPriceTag = web_page.find("span", {"itemprop": "price"})
    doc_findPriceTag_contents = doc_findPriceTag.text
    float_doc_findPriceTag_contents = "%.2f" % float(doc_findPriceTag_contents.replace(",", ""))

    doc_findNameTag = web_page.find("h1", {"itemprop": "name"})
    doc_findNameTag_contents = doc_findNameTag.text

    doc_findImageTag = web_page.find("img", {"alt": "product pic"})
    doc_findImageTag_attURL = doc_findImageTag["src"]

    info = {
        'name': doc_findNameTag_contents,
        'price': float_doc_findPriceTag_contents,
        'img': doc_findImageTag_attURL,
        'href': url
    }

    return info



