from datetime import datetime
from pracownicy import Kasjer
from zwierzaki import Zwierze
from pracownicy import Pracownik


class ZOO:
    def __init__(self) -> None:
        self.zwierzeta = []
        self.pracownicy = []

    def dodaj_zwierze(self, zwierze: Zwierze) -> None:
        self.zwierzeta.append(zwierze)

    def dodaj_pracownika(self, pracownik: Pracownik) -> None:
        self.pracownicy.append(pracownik)

    def pokaz_zwierzeta(self) -> str:
        if not self.zwierzeta:
            return "Brak zwierząt"
        return "\n".join(str(zwierze) for zwierze in self.zwierzeta)

    def pokaz_pracownikow(self) -> str:
        if not self.pracownicy:
            return "Brak pracowników"
        return "\n".join(str(pracownik) for pracownik in self.pracownicy)


class Klient:
    def __init__(self, name: str, has_a_ticket: bool) -> None:
        self.has_a_ticket = has_a_ticket
        self.name = name


class Kasa:
    def __init__(self, kasjer: Kasjer) -> None:
        self.kasjer = kasjer

    def kup_bilet(self, klient: Klient) -> str:
        aktualna_godzina = datetime.now().hour

        if 8 <= aktualna_godzina < 19:
            return f"{self.kasjer.imie} sprzedał bilet dla {klient}."
        else:
            return "Kasa jest zamknięta. Można kupić bilet od 8:00 do 19:00."
