from abc import ABC, abstractmethod

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
            dodatki = ", ".join(f"{k}: {v}" for k,
                                v in self.dodatkowe_info.items())
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
