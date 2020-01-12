import bs4
from bs4 import BeautifulSoup as soup
try:
    from urllib.request import Request, urlopen
except ImportError:
    from urllib2 import Request, urlopen

target = "Black Clover"

def format_t(target):
    return target.lower().replace(" ", "_")

url = 'https://manganelo.com/search/' + format_t(target)

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

print(get_update(target,url))
