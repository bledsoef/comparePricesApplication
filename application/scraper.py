from bs4 import BeautifulSoup as bs
import re
import requests

def formatUserInput(text):
    formattedText = text.replace("", "+")
    return formattedText

def runScraper(productInput, priceInput):
    scraper = initializeFirstScraper(formatUserInput(productInput))
    urlList = getUrls(scraper, productInput)
    pricesList = getPrices(urlList)
    comparePrices(pricesList, priceInput)

def initializeFirstScraper(userInput):

    response = requests.get('https://www.ebay.com/sch/i.html?_nkw=' + userInput)
    soup = bs(response.text, 'html.parser')
    return soup

def initializeFollowingScraper(url):
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    return soup


def getUrls(scraper, userInput):
    urlList=[]
    for tag in scraper.find_all('a', href=True):
        if ("/search?q=" + userInput) or "maps" or "settings" or "advanced_search" or "policies" not in tag['href']:
            urlList.append(tag['href'])
    return urlList

def getPrices(urls):
    for url in urls:
        try:
            if "http" in url:
                scraper=initializeFollowingScraper(url[7:])
                pricesOnPage = re.findall("$", scraper)
                print(pricesOnPage)
        except Exception as e:
            print(e)

def comparePrices(pricesList):
    pass
            