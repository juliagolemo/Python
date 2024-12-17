# musimy najpierw zdefiniowac funkcje!! inaczej nam ja bedzie podkreslac

def begruessung():
    print("Hallo, nett dich kennenzulernen!")
begruessung()

# Tekst wyswietla nam sie w terminalu
# Dlaczego print działa przez funkcję begruessung()?
# kiedy pisze def, print, to dopiero TWORZE funkcje o nazwie begruessung.
# Jednak samo zdefiniowanie funkcji niczego nie wykonuje.
# dopiero kiedy napisze begruessung(), czyli WYWOLAM funckcje, wszystko sie wykonuje
# podsumowanie
# def definiuje funkcję, czyli przygotowuje pewne instrukcje do późniejszego wykonania.
# Wywołanie funkcji (np. begruessung()) sprawia, że instrukcje w funkcji są wykonywane.
# W środku funkcji może znajdować się print, ale to begruessung() wywołuje ten print.

begruessung()
begruessung()
begruessung()

# To po co pisac funkcje, skoro mozna print i na to samo wyjdzie?
# Po to zeby szybciej wyswietlac zawartosc - czyli nie musimy calego dlugiego print za kazdym razem pisac
# Wystraczy begruessung() i mamy

def begruessung(name):
    print("Hallo", name, ", nett dich kennenzulernen!")
begruessung("Julia")
begruessung("Sabine")
begruessung("Anna")

def begruessung(name, alter):
    print("Hallo", name, ", nett dich kennenzulernen! Du bist", alter, "Jahre alt.")
begruessung("Julia", 23)
