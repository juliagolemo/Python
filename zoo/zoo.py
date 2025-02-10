from abc import ABC, abstractmethod

class Zwierze(ABC):
    def __init__(self, imie: str, wiek: int, waga: float, wzrost: float):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost

    def __str__(self):
        return f"{self.imie}, Wiek: {self.wiek} lat, Waga: {self.waga} kg, Wzrost: {self.wzrost} cm"

    @abstractmethod
    def daj_glos(self):
        pass

class Zwierze_Ladowe(Zwierze):
    def biegnij(self):
        szybkosc_biegu = (self.waga / 10) + (self.wzrost / 5)
        return f"{self.imie} biegnie z prędkością {szybkosc_biegu:.2f} km/h"

class Zwierze_Latajace(Zwierze_Ladowe):
    def __init__(self, imie: str, wiek: int, waga: float, wzrost: float, rozpietosc_skrzydel: float):
        super().__init__(imie, wiek, waga, wzrost)
        self.rozpietosc_skrzydel = rozpietosc_skrzydel

    def lec(self):
        szyb_lotu = (self.waga / 5) + (self.wzrost / 2)
        return f"{self.imie} leci z prędkością {szyb_lotu:.2f} km/h"

class Pies(Zwierze_Ladowe):
    def daj_glos(self):
        return "Hau hau"

class Krolik(Zwierze_Ladowe):
    def daj_glos(self):
        return "Piiii"

class Kot(Zwierze_Ladowe):
    def daj_glos(self):
        return "Miau"

class Pelikan(Zwierze_Latajace):
    def __init__(self, imie, wiek, waga, wzrost, rozpietosc_skrzydel):
        super().__init__(imie, wiek, waga, wzrost, rozpietosc_skrzydel)

    def daj_glos(self):
        return "Blyyyyb"

class Sikorka(Zwierze_Latajace):
    def __init__(self, imie, wiek, waga, wzrost, rozpietosc_skrzydel):
        super().__init__(imie, wiek, waga, wzrost, rozpietosc_skrzydel)

    def daj_glos(self):
        return "Ćwir"

pies = Pies("Czika", 9, 10, 40)
krolik = Krolik("Pabi", 7, 2, 20)
kot = Kot("Szeszyr", 9, 5, 17)
pelikan = Pelikan("Renia", 3, 8, 100, 1.9)
sikorka = Sikorka("Sikorinda", 1, 0.11, 11.5, 21.0)

print(pies.daj_glos(), pies)
print(krolik.daj_glos(), krolik)
print(kot.daj_glos(), kot)

print(pies.biegnij())
print(krolik.biegnij())
print(kot.biegnij())

print(pelikan.daj_glos(), pelikan)
print(pelikan.lec())

print(sikorka.daj_glos(), sikorka)
print(sikorka.lec())

class ZOO:
    def __init__(self):
        self.zwierzeta = []

    def dodaj_zwierze(self, zwierze: Zwierze):
        self.zwierzeta.append(zwierze)

    def pokaz_zwierzeta(self):
        if not self.zwierzeta:
            return "Brak zwierząt"
        return "\n".join(str(zwierze) for zwierze in self.zwierzeta)

moje_zoo = ZOO()
moje_zoo.dodaj_zwierze(pies)
moje_zoo.dodaj_zwierze(kot)
moje_zoo.dodaj_zwierze(pelikan)
moje_zoo.dodaj_zwierze(sikorka)

print("\nZwierzęta w zoo:")
print(moje_zoo.pokaz_zwierzeta())


from abc import ABC, abstractmethod

class Pracownik(ABC):
    def __init__(self, imie: str, nazwisko: str):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f"{self.imie} {self.nazwisko} - {self.__class__.__name__}"

    @abstractmethod
    def wykonaj_prace(self):
        pass

class OpiekunZwierzat(Pracownik):
    def wykonaj_prace(self):
        return "Opiekuję się zwierzętami"

    def nakarm_zwierze(self, zwierze, ilosc_jedzenia):
        zwierze.waga += ilosc_jedzenia * 0.1  # Każde 1 kg jedzenia zwiększa wagę o 0.1 kg
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

opiekun = OpiekunZwierzat("Julian", "Golemowski")
sprzatacz = Sprzatacz("Kazimierz", "Nowak")
kasjer = Kasjer("Kazia", "Wiśniewska")

