import mangaBot as mb
import mangaList as ml

mangas = ml.read_mangas("teste.txt")

for manga in mangas:
    print(f"{manga} {mb.get_update(manga)}")
