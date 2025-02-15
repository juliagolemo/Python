from datetime import datetime
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


