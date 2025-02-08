from abc import ABC, abstractmethod

# Klasa abstrakcyjna Zwierze


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

# Klasa Zwierze_Ladowe dziedzicząca po Zwierze


class Zwierze_Ladowe(Zwierze):
    def biegnij(self):
        szybkosc_biegu = (self.waga / 10) + (self.wzrost / 5)
        return f"{self.imie} biegnie z prędkością {szybkosc_biegu:.2f} km/h"

# Klasa Zwierze_Latajace dziedzicząca po Zwierze


class Zwierze_Latajace(Zwierze):
    def __init__(self, imie: str, wiek: int, waga: float, wzrost: float, rozpietosc_skrzydel: float):
        super().__init__(imie, wiek, waga, wzrost)
        self.rozpietosc_skrzydel = rozpietosc_skrzydel

    def lec(self):
        szyb_lotu = (self.waga / 5) + (self.wzrost / 2)
        return f"{self.imie} leci z prędkością {szyb_lotu:.2f} km/h"


class Pies(Zwierze_Ladowe):
    def daj_glos(self):
        return "Hau hau"

pies = Pies("Czika", 9, 10, 40)
print(pies.daj_glos())
print(pies)

class Krolik(Zwierze_Ladowe):
    def daj_glos(self):
        return "Piiii"


krolik = Krolik("Pabi", 7, 2, 20)
print(krolik.daj_glos())
print(krolik)

print(pies.biegnij())
print(krolik.biegnij())

class Kot(Zwierze_Ladowe):
    def daj_glos(self):
        return "Miau"


kot = Kot("Szeszyr", 9, 5, 17)
print(kot.daj_glos())
print(kot)

print(kot.biegnij())

class Pelikan(Zwierze_Latajace):
    def daj_glos(self):
        return "Blyyyyb"

    def lec(self):
        szyb_lotu = (self.waga / 5) + (self.wzrost / 2)
        return f"{self.imie} leci z prędkością {szyb_lotu:.2f} km/h"

pelikan = Pelikan("Renia", 3, 8, 100, 1.9)
print(pelikan.lec())
print(pelikan)

print(pelikan.lec())

class Sikorka(Zwierze_Latajace):
    def daj_glos(self):
        return "Ćwir"

sikorka = Sikorka("Sikorinda", 1, 0.11, 11.5, 21)
print(sikorka.lec())
print(sikorka)

class ZOO:
    def __init__(self):
        self.zwierzeta = []


