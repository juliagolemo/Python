from abc import ABC, abstractmethod
from datetime import datetime

class Zwierze(ABC):
    def __init__(self, imie: str, wiek: int, waga: float, wzrost: float, *args, **kwargs):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.dodatkowe_info = kwargs  # Dodatkowe info

    def __str__(self):
        opis = f"{self.imie}, Wiek: {self.wiek} lat, Waga: {self.waga} kg, Wzrost: {self.wzrost} cm"
        if self.dodatkowe_info:
            dodatki = ", ".join(f"{k}: {v}" for k, v in self.dodatkowe_info.items())
            opis += f" ({dodatki})"
        return opis

    @abstractmethod
    def daj_glos(self):
        pass


class Zwierze_Ladowe(Zwierze):
    def __init__(self, imie, wiek, waga, wzrost, *args, **kwargs):
        super().__init__(imie, wiek, waga, wzrost, *args, **kwargs)

    def biegnij(self):
        szybkosc_biegu = (self.waga / 10) + (self.wzrost / 5)
        return f"{self.imie} biegnie z prędkością {szybkosc_biegu:.2f} km/h"


class Zwierze_Latajace(Zwierze_Ladowe):
    def __init__(self, imie, wiek, waga, wzrost, rozpietosc_skrzydel, *args, **kwargs):
        super().__init__(imie, wiek, waga, wzrost, *args, **kwargs)
        self.rozpietosc_skrzydel = rozpietosc_skrzydel

    def lec(self):
        szyb_lotu = (self.waga / 5) + (self.wzrost / 2)
        return f"{self.imie} leci z prędkością {szyb_lotu:.2f} km/h"


class Pies(Zwierze_Ladowe):
    def daj_glos(self):
        return "Hau hau"


class Kot(Zwierze_Ladowe):
    def daj_glos(self):
        return "Miau"


class Pelikan(Zwierze_Latajace):
    def daj_glos(self):
        return "Blyyyyb"


class Pracownik(ABC):
    def __init__(self, imie: str, nazwisko: str, *args, **kwargs):
        self.imie = imie
        self.nazwisko = nazwisko
        self.dodatkowe_info = kwargs

    def __str__(self):
        opis = f"{self.imie} {self.nazwisko} - {self.__class__.__name__}"
        if self.dodatkowe_info:
            dodatki = ", ".join(f"{k}: {v}" for k, v in self.dodatkowe_info.items())
            opis += f" ({dodatki})"
        return opis

    @abstractmethod
    def wykonaj_prace(self):
        pass


class OpiekunZwierzat(Pracownik):
    def wykonaj_prace(self):
        return "Opiekuję się zwierzętami."

    def nakarm_zwierze(self, zwierze, ilosc_jedzenia):
        zwierze.waga += ilosc_jedzenia * 0.1
        return f"{self.imie} nakarmił {zwierze.imie}, nowa waga: {zwierze.waga:.2f} kg."


class Sprzatacz(Pracownik):
    def wykonaj_prace(self):
        return "Sprzątam zoo."

    def sprzataj(self):
        return f"{self.imie} sprząta zoo."


class Kasjer(Pracownik):
    def wykonaj_prace(self):
        return "Sprzedaję bilety."

    def sprzedaj_bilet(self, klient):
        return f"{self.imie} sprzedał bilet dla {klient}."


class Dyrektor(Pracownik):
    def wykonaj_prace(self):
        return "Zarządzam zoo."

    def zarzadzaj(self):
        return f"{self.imie} zarządza zoo."


class Weterynarz(Pracownik):
    def wykonaj_prace(self):
        return "Leczę zwierzęta."

    def lecz(self):
        return f"{self.imie} leczy zwierzęta."


class ZOO:
    def __init__(self):
        self.zwierzeta = []
        self.pracownicy = []

    def dodaj_zwierze(self, zwierze):
        self.zwierzeta.append(zwierze)

    def dodaj_pracownika(self, pracownik):
        self.pracownicy.append(pracownik)

    def pokaz_zwierzeta(self):
        if not self.zwierzeta:
            return "Brak zwierząt"
        return "\n".join(str(zwierze) for zwierze in self.zwierzeta)

    def pokaz_pracownikow(self):
        if not self.pracownicy:
            return "Brak pracowników"
        return "\n".join(str(pracownik) for pracownik in self.pracownicy)


class Kasa:
    def __init__(self, kasjer):
        self.kasjer = kasjer

    def kup_bilet(self, klient):
        teraz = datetime.now().hour

        if 8 <= teraz < 19:
            return f"{self.kasjer.imie} sprzedał bilet dla {klient}."
        else:
            return "Kasa jest zamknięta. Można kupić bilet od 8:00 do 19:00."


pies = Pies("Czika", 9, 10, 40, rasa="Kundelek", ulubiony_posilek="Mieso")
kot = Kot("Szeszyr", 9, 5, 17, ulubiona_zabawa="Polowanie")
pelikan = Pelikan("Renia", 3, 8, 100, 1.9, kraj_pochodzenia="Brazylia")

opiekun = OpiekunZwierzat("Julian", "Golemowski", staz=5, specjalizacja="Ssaki")
sprzatacz = Sprzatacz("Kazimierz", "Nowak", staz=3)
kasjer = Kasjer("Kazia", "Wiśniewska", zmiana="Poranna")
dyrektor = Dyrektor("Wojciech", "Kocur", doswiadczenie=15)
weterynarz = Weterynarz("Weronika", "Stonoga", specjalizacja="Ssaki")

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
