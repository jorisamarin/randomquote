import requests
from bs4 import BeautifulSoup

def getQuotes():

    URL = "https://ircquotes.fi/list.php?sort=rand"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="maintd")


    quotes = results.find_all("div", class_="quote")
    quoteDict = {"quote": []}
    for quote in quotes:
        quoteDict["quote"] = quote.text
        
    return quoteDict

