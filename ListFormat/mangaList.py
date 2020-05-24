def read_mangas(mangas):
    """"Build a list with the mangas names.""

    l = []
    with open(mangas) as m:
        for manga in m:
            l.append(manga.rstrip())
    return l
