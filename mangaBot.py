import bs4
import re
from bs4 import BeautifulSoup as soup
try:
    from urllib.request import Request, urlopen
except ImportError:
    from urllib2 import Request, urlopen

sites = []
with open("sites.txt") as l:
    for link in l:
        sites.append(link.rstrip())
urls = dict(enumerate(sites))



def format_t(target):
    return re.sub('[^A-Za-z0-9 ]+','',target.lower()).replace(" ", "_")


def url(target,index=0):
    return urls[index] + format_t(target)

def get_update(target,index=0):
    req = Request(url(target,index), headers={'User-Agent': 'Mozilla/5.0'})
    update = "None"
    uClient = urlopen(req)
    webpage = uClient.read()
    uClient.close()
    page = soup(webpage,"html.parser")
    mangas = page.findAll("div",{"class": "search-story-item"});
    for manga in mangas:
        if target.lower() == manga.div.a.text.lower():
            update = manga.find("span",{"class": "text-nowrap item-time"}).text
    return update
