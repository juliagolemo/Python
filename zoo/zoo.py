from abc import ABC, abstractmethod


class Zwierze(ABC):
    def __init__(self, imie: str, wiek: int, waga: float, wzrost: float, *args, **kwargs):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.dodatkowe_info = kwargs  # Przechowuje dodatkowe informacje

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
    def biegnij(self):
        szybkosc_biegu = (self.waga / 10) + (self.wzrost / 5)
        return f"{self.imie} biegnie z prędkością {szybkosc_biegu:.2f} km/h"


class Pracownik(ABC):
    def __init__(self, imie: str, nazwisko: str, *args, **kwargs):
        self.imie = imie
        self.nazwisko = nazwisko
        self.dodatkowe_info = kwargs
# Dzieki kwargs mozemy dodc dodatkowe info jak np. staż pracy, specjalizację itd.

    def __str__(self):
        opis = f"{self.imie} {self.nazwisko} - {self.__class__.__name__}"
        if self.dodatkowe_info:
            dodatki = ", ".join(f"{k}: {v}" for k, v in self.dodatkowe_info.items())
            opis += f" ({dodatki})"
        return opis

    @abstractmethod
    def wykonaj_prace(self):
        pass

    @abstractmethod
    def daj_opis_pracy(self):
        pass


class OpiekunZwierzat(Pracownik):
    def wykonaj_prace(self):
        return "Opiekuję się zwierzętami."

    def daj_opis_pracy(self):
        return "Zajmuje się karmieniem i dbaniem o zwierzęta w zoo."

    def nakarm_zwierze(self, zwierze, ilosc_jedzenia):
        zwierze.waga += ilosc_jedzenia * 0.1
        return f"{self.imie} nakarmił {zwierze.imie}, nowa waga: {zwierze.waga:.2f} kg."


class Sprzatacz(Pracownik):
    def wykonaj_prace(self):
        return "Sprzątam zoo."

    def daj_opis_pracy(self):
        return "Odpowiada za czystość w zoo, sprząta klatki i alejki."

    def sprzataj(self):
        return f"{self.imie} sprząta zoo."


class Kasjer(Pracownik):
    def wykonaj_prace(self):
        return "Sprzedaję bilety."

    def daj_opis_pracy(self):
        return "Sprzedaje bilety odwiedzającym zoo."

    def sprzedaj_bilet(self, klient):
        return f"{self.imie} sprzedał bilet dla {klient}."


class Dyrektor(Pracownik):
    def wykonaj_prace(self):
        return "Zarządzam zoo."

    def daj_opis_pracy(self):
        return "Kieruje całą działalnością zoo, nadzoruje pracowników."

    def zarzadzaj(self):
        return f"{self.imie} zarządza zoo."


class Weterynarz(Pracownik):
    def wykonaj_prace(self):
        return "Leczę zwierzęta."

    def daj_opis_pracy(self):
        return "Opiekuje się zdrowiem zwierząt, przeprowadza badania i leczenie."

    def lecz(self):
        return f"{self.imie} leczy zwierzęta."


# Dzieki kwargs mamy tu juz dodatkowe dane jak np. specjalizacja, albo zmiana pracy
opiekun = OpiekunZwierzat("Julian", "Golemowski", staz=5, specjalizacja="Ssaki")
sprzatacz = Sprzatacz("Kazimierz", "Nowak", staz=3)
kasjer = Kasjer("Kazia", "Wiśniewska", zmiana="Poranna")
dyrektor = Dyrektor("Wojciech", "Kocur", doswiadczenie=15)
weterynarz = Weterynarz("Weronika", "Stonoga", specjalizacja="Ssaki")

# Tworzenie zwierząt z dodatkowymi danymi
pies = Zwierze_Ladowe("Czika", 9, 10, 40, rasa="Labrador", ulubiony_posilek="Kości")
krolik = Zwierze_Ladowe("Pabi", 7, 2, 20, ulubiona_zabawa="Kopanie norek")

pracownicy = [opiekun, sprzatacz, kasjer, dyrektor, weterynarz]

print("\nOpisy pracowników:")
for pracownik in pracownicy:
    print(f"{pracownik}: {pracownik.daj_opis_pracy()}")

zwierzeta = [pies, krolik]

print("\nZwierzęta w zoo:")
for zwierze in zwierzeta:
    print(zwierze)
