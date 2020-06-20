import Scraping.mangaBot as mb
import ListFormat.mangaList as ml
import sys


def get_updates(sites):
    """Build a list of the mangas' updates."""

    mangas = ml.read_mangas("./mangas.txt")
    l = dict();
    for manga in mangas:
        l[manga] = mb.get_update(manga)
    return l



if __name__ =="__main__":
    mangas = ml.read_mangas("./mangas.txt")
    if(len(sys.argv) == 1):
        for manga in mangas:
            print(f"{manga:50} {mb.get_update(manga)}")

    elif(sys.argv[1] == "-s" or sys.argv[1] == "--show"):
        ml.show_mangas(mangas)

    elif(sys.argv[1] == "-a" or sys.argv == "--append"):
        ml.append_mangas(sys.argv,"./mangas.txt")

    elif(sys.argv[1] == "-r" or sys.argv == "--remove"):
        if(not sys.argv[2].isdigit()):
            ml.remove_manga("./mangas.txt",name = sys.argv[2])
        else:
            ml.remove_manga("./mangas.txt",index = int(sys.argv[2]))
