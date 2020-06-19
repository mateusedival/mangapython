import bs4
import re
from bs4 import BeautifulSoup as soup
import requests

sites = []
with open("./sites.txt") as l:
    for link in l:
        sites.append(link.rstrip())
urls = dict(enumerate(sites))

def format_target(target):
    """Format the target to append to the url."""

    return re.sub('[^A-Za-z0-9 ]+','',target.lower()).replace(" ", "_")

def formart_title(title):
    """Format the title to be only lower letters and remove whitespaces."""

    return re.sub('[^A-Za-z0-9]+','',title.lower())


def url(target,index=0):
    """Return the target url of the index website."""

    return urls[index] + format_target(target)

def get_update(target,index=0):
    """Get the target last update info on the index site."""

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    req = requests.get(url(target,index), headers=headers)
    update = "None"
    found = False
    page = soup(req.content,"html.parser")
    mangas = page.findAll("div",{"class": "search-story-item"});

    for manga in mangas:
        if formart_title(target) == formart_title(manga.div.a.text):
            found = True
            update = manga.find("span",{"class": "text-nowrap item-time"}).text
    if found == False:
        update = "Not Found"
    return update
