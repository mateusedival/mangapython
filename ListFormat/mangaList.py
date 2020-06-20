def read_mangas(mangas):
    """Build a list with the mangas names."""

    l = []
    with open(mangas) as m:
        for manga in m:
            l.append(manga.rstrip())
    return l

#adicionar as docstrings que faltam

def append_mangas(new_manga,mangas):
    buffer = ""
    with open(mangas, "a") as file:
        for i in range(2,len(new_manga)):
            buffer += new_manga[i]
            if(i != len(new_manga) - 1):
                buffer += ' '
        file.write(buffer+'\n')

def show_mangas(mangaList):
    for manga in mangaList:
        print(manga)

def remove_manga(mangas,index = -1,name = "none"):
    mangaList = read_mangas(mangas)

    #atualizar para ficar igual append_mangas
    if(name != "none"):
        for manga in mangaList:
            if(manga == name.rstrip()):
                mangaList.remove(manga)

    if(name == "last"):
        mangaList.pop()

    if(index != -1):
        mangaList.pop(index-1)

    buffer = ""
    for manga in mangaList:
        buffer += (str(manga) + '\n')

    with open(mangas,"w") as file:
        file.write(buffer)
