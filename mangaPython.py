import Scraping.mangaBot as mb
import ListFormat.mangaList as ml


def get_updates(sites):
    """Build a list of the mangas' updates."""

    mangas = ml.read_mangas("./mangas.txt")
    l = dict();
    for manga in mangas:
        l[manga] = mb.get_update(manga)
    return l



if __name__ =="__main__":
    mangas = ml.read_mangas("./mangas.txt")
    for manga in mangas:
        print(f"{manga:50} {mb.get_update(manga)}")
