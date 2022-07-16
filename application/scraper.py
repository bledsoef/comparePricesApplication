from bs4 import BeautifulSoup as bs
import requests

def runScraper(userInput):
    scraper = initializeFirstScraper(userInput)
    urlList = getUrls(scraper, userInput)
    getPrices(urlList)

def initializeFirstScraper(userInput):
    response = requests.get('https://www.google.com/search?q=' + userInput)
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
                pricesOnPage = scraper.find_all("div", class_ ="price")
                print(url[7:])
                print(pricesOnPage)
        except Exception as e:
            print(e)
            