
def read_mangas(mangas):
    l = []
    with open(mangas) as m:
        for manga in m:
            l.append(manga.rstrip())
    return l
