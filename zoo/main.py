from datetime import datetime
from zwierzaki import Pies, Kot, Pelikan
from zoo import ZOO, Kasa
from pracownicy import OpiekunZwierzat, Sprzatacz, Kasjer, Dyrektor, Weterynarz


opiekun = OpiekunZwierzat("Julian", "Golemowski",
                          staz=5, specjalizacja="Ssaki")
sprzatacz = Sprzatacz("Kazimierz", "Nowak", staz=3)
kasjer = Kasjer("Kazia", "Wiśniewska", zmiana="Poranna")
dyrektor = Dyrektor("Wojciech", "Kocur", doswiadczenie=15)
weterynarz = Weterynarz("Weronika", "Stonoga", specjalizacja="Ssaki")

pies = Pies("Czika", 9, 10, 40, rasa="Kundelek", ulubiony_posilek="Mieso")
kot = Kot("Szeszyr", 9, 5, 17, ulubiona_zabawa="Polowanie")
pelikan = Pelikan("Renia", 3, 8, 100, 1.9, kraj_pochodzenia="Brazylia")

moje_zoo = ZOO()
moje_zoo.dodaj_zwierze(pies)
moje_zoo.dodaj_zwierze(kot)
moje_zoo.dodaj_zwierze(pelikan)
moje_zoo.dodaj_pracownika(opiekun)
moje_zoo.dodaj_pracownika(sprzatacz)
moje_zoo.dodaj_pracownika(kasjer)

kasa = Kasa(kasjer)

print("\nPracownicy zoo:")
print(moje_zoo.pokaz_pracownikow())

print("\nZwierzęta w zoo:")
print(moje_zoo.pokaz_zwierzeta())

print("\nKupowanie biletu:")
print(kasa.kup_bilet("Klient 1"))
