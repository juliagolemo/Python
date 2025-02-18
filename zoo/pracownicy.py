from abc import ABC, abstractmethod


class Pracownik(ABC):
    def __init__(self, imie: str, nazwisko: str, *args, **kwargs):
        self.imie = imie
        self.nazwisko = nazwisko
        self.dodatkowe_info = kwargs

    def __str__(self):
        opis = f"{self.imie} {self.nazwisko} - {self.__class__.__name__}"
        if self.dodatkowe_info:
            dodatki = ", ".join(f"{k}: {v}" for k,
                                v in self.dodatkowe_info.items())
            opis += f" ({dodatki})"
        return opis

    @abstractmethod
    def wykonaj_prace(self, *args, **kwargs):
        pass


class OpiekunZwierzat(Pracownik):
    def __init__(self, imie, nazwisko, staz, specjalizacja):
        super().__init__(imie, nazwisko)
        self.staz = staz
        self.specjalizacja = specjalizacja

    def wykonaj_prace(self, zwierze, ilosc_jedzenia):
        return self.nakarm_zwierze(zwierze=zwierze, ilosc_jedzenia=ilosc_jedzenia)

    def nakarm_zwierze(self, zwierze, ilosc_jedzenia):
        zwierze.waga += ilosc_jedzenia * 0.1
        return f"{self.imie} nakarmił {zwierze.imie}, nowa waga: {zwierze.waga:.2f} kg."


class Sprzatacz(Pracownik):
    def __init__(self, imie, nazwisko, staz):
        super().__init__(imie, nazwisko)
        self.staz = staz

    def wykonaj_prace(self, miejsce, czas):
        return self.sprzataj(miejsce=miejsce, czas=czas)

    def sprzataj(self, miejsce, czas):
        return f"{self.imie} {self.nazwisko} sprząta {miejsce} przez {czas} minut."


class Kasjer(Pracownik):
    def __init__(self, imie, nazwisko, zmiana):
        super().__init__(imie, nazwisko)
        self.zmiana = zmiana

    def wykonaj_prace(self, klient, cena):
        return self.sprzedaj_bilet(klient=klient, cena=cena)

    def sprzedaj_bilet(self, klient, cena):
        return f"{self.imie} {self.nazwisko} sprzedał(a) bilet dla {klient} za {cena} zł."


class Dyrektor(Pracownik):
    def __init__(self, imie, nazwisko, doswiadczenie):
        super().__init__(imie, nazwisko)
        self.doswiadczenie = doswiadczenie

    def wykonaj_prace(self, dzial, decyzja):
        return self.zarzadzaj(dzial=dzial, decyzja=decyzja)

    def zarzadzaj(self, dzial, decyzja):
        return f"{self.imie} {self.nazwisko} zarządza działem {dzial} i podjął decyzję: {decyzja}."


class Weterynarz(Pracownik):
    def __init__(self, imie, nazwisko, specjalizacja):
        super().__init__(imie, nazwisko)
        self.specjalizacja = specjalizacja

    def wykonaj_prace(self, zwierze, choroba):
        return self.lecz(zwierze=zwierze, choroba=choroba)

    def lecz(self, zwierze, choroba):
        return f"{self.imie} {self.nazwisko}, specjalista od {self.specjalizacja}, leczy {zwierze} na {choroba}."
