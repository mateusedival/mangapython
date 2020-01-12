import bs4
#from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

from urllib.request import Request, urlopen

target = input("Target: ")

def treat_target(target):
    for i in target:
        if target[i] == " ":
            target[i] == "_"

print(treat_target(target))

#url = 'https://manganelo.com/search/{}'.format(treated_target)

def get_update(target,url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    update = "None"
    uClient = urlopen(req)
    webpage = uClient.read()
    uClient.close()
    page = soup(webpage,"html.parser")
    mangas = page.findAll("div",{"class": "search-story-item"});
    for manga in mangas:
        if target == manga.div.a["title"]:
            update = manga.find("span",{"class": "text-nowrap item-time"}).text
    return update

#print(get_update(target,url))
