# OOP to sposób pisania programów
# Wyobraź sobie, że tworzysz program o samochodach. W OOP każdy samochód to obiekt. Obiekt ma:
# Cechy (czyli właściwości) – np. kolor, markę, liczbę kół.
# Umiejętności (czyli metody) – np. "jedź", "zatrzymaj się", "włącz światła".
# Te obiekty powstają na podstawie klasy, czyli takiego przepisu albo szablonu.
# Klasa mówi, jakie cechy i umiejętności będzie miał każdy samochód.
# Klasy piszemy duzymy literami (class Auto / class MeineAuto)

class Auto():
    pass

# help(Auto)
# Tutaj tworze klasę o nazwie Auto
# pass – oznacza "nic tu jeszcze nie ma". Python wymaga, żeby coś było w środku klasy, więc pass jest takim "zapychaczem" na później. Klasa istnieje, ale nie ma jeszcze żadnych cech ani metod.
# help(Auto) - help() to wbudowana funkcja w Pythonie, która pokazuje dokumentację obiektu
# Efekt tego wywołania: Python wyświetli podstawowe informacje o klasie Auto


class Auto():
    raeder = 4
    tueren = 2


auto1 = Auto()
print(auto1.raeder)

# hcemy zmienic drzwi, bo nie kazde auto ma 2 drzwi
# Zawsze musi byc to self!!


class Auto():
    def __init__(self, marke, modell, baujahr, raeder, tueren):
        self.marke = marke
        self.modell = modell
        self.jakr = jahr
        self.raeder = 4
        self.tueren = tueren
