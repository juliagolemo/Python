# To jest proste rownanie. Print tylko wyświetla wynik na ekranie i nie mozna juz go dalej uzywac w obliczeniach.
def addieren(a, b):
    print(a + b)
addieren(20, 5)
# Otrzymujemy wynik

# Zawsze, gdy chce dalej chce liczyc, dalej uzywac otrzymanego wyniku, musze zrobic to return
def addieren(a, b):
    return a + b
summe = addieren(7, 8)
print(summe)

def hallo(name, alter):
    print(name)
    print(alter)
hallo(name "Julia", alter:23)
# Wyswietla nam sie po kolei imie, potem wiek

# Tez nam sie po kolei wyswietla
def hallo(name = "Chiara", alter = 85):
    print(name)
    print(alter)
hallo()

# Moge tez tak:
def hallo(name = "Chiara", alter = 85):
    print(name)
    print(alter)
hallo(name = "Chiara", alter=85 )

# Co jesli nie wiemy ile np liczb chcemy dodac? Wtedy po prostu dodaje zahlen ale z GWIAZDKA!!jesli nie wiem, ile czegos bedzie/jest, dodaje gwiazdke
# Jak nie znam liczby argumentow -> gwiazdka

def addieren(*zahlen):
    print(sum(zahlen))
addieren(20, 80, 6)
# czemu w tutorialu byl : a tu nie moge miec, bo mi inaczej nie wychodzi?? okolo 3h 20min

# ** daje wtedy, jak cos juz bylo wczesniej zdefiniowane
def addieren(**daten):
    print(daten)
addieren(name = "Julia", alter = 23, hobby = "turnen")

# DOCSTRINGS - längere Kommentare
"""
ofjoerf
""""
