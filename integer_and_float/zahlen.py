# INTGER - angegeben als int, Ganzzahlen, positiv oder negativ z.B. 100, 20, 0, -50
# FLOAT z.B. 3.6, 8.9
#FUNKTION type - einfache Funktion zur Bestimmung des Datentyps (int, float usw.)

print(10 / 2)
print(type(10))
print(type(5.0))
print(type(10 / 2))

# DIVISION MIT REST (sprawdzamy czy równanie ma reszte)
# Beispiel: 11/2 = 2 Rest 1
# (11 % 2) -> 1

# Otrzymujemy 3.3333333333333335
print(10 / 3)
# Wychodzi, ze ma reszte 1
print(10 % 3) 

print(10 / 2)
print(11 % 3)

# POTEGI
print(10 ** 2)
print(10 ** 0.5)

#NUTZEREINGABE - werden in Python mit input() realisiert
# Wyswietla sie nam to zdanie w terminalu
x = input("Wie ist dein Name?")
# Zeby proces byl "dokonczon", dopisujemy odpowiedz w TERMINALU np. Wie ist dein Name?Julia

# Co jesli chcemy wyswietlic x? Piszemy w terminalu imie, odpalami i wyswietla sie samo imie 
x = input("Wie ist dein Name?")
print(x)

# Wyswietla sie Hallo Julia
print("Hallo " + x)

y = input("Wie viel ist dein Ausgangsgehalt? ") 
x = y * 1.10
print(x)

# 1.10, weil es ist die 10prozentige Gehaltserhoeung hier verarbeitet
# to samo tutaj - wpisujac liczbe w terminalu - nie dziala!!!

#Projekt - Waehrungs-Umrechner
# float, bo moga byc liczby po przecinku
# baht to tajska waluta
euro = float(input("Wie viel Euro hast du? "))
baht = euro * 38.06
print("Super! Deine ", euro, " Euro sind ", baht, " Baht wert.")