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

# Klasa Zwierze_Latajace dziedzicząca po Zwierze_Ladowe
class Zwierze_Latajace(Zwierze_Ladowe):
    def __init__(self, imie: str, wiek: int, waga: float, wzrost: float, rozpietosc_skrzydel: float):
        super().__init__(imie, wiek, waga, wzrost)
        self.rozpietosc_skrzydel = rozpietosc_skrzydel

    def lec(self):
        szyb_lotu = (self.waga / 5) + (self.wzrost / 2)
        return f"{self.imie} leci z prędkością {szyb_lotu:.2f} km/h"
