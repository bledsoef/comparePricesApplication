from bs4 import BeautifulSoup as bs
import requests

def runScraper(input):
    urlList=[]
    scraper = initializeScraper(input)
    for a in scraper.find_all('a', href=True):
        if ("/search?q=" + input) or "maps" or "settings" or "advanced_search" or "policies" not in a['href']:
            urlList.append(a['href'])
    print(len(urlList))

def initializeScraper(input):
    response = requests.get('https://www.google.com/search?q=' + input)
    soup = bs(response.text, 'html.parser')
    return soup