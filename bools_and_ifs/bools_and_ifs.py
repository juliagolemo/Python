# Booleans (Wahrheitswerte)

print(type(True))
# Wir bekommen <class 'bool'>

print(type(False))
# Wir bekommen <class 'bool'>


print(type(2 > 1))
# Wir bekommen wieder <class 'bool'>

# Wiemy juz, ze to bool wiec mozemy type usunac
print(2 > 1)
# Wir bekommen True

print(2 < 1)
print(9 < 2)

# Jak sprawdzic, czy wartosci sa rowne? (PRZY BOOLS UZYWAMY ==)
print(2 == 2)

# Wenn...dann

# tutaj daje tylko jedno =, bo to zmienna, a nie bool
streckeInKm = 2

# Pamietac o dwukropku!!! Potem wazne jest zeby byla zachowana przerwa, akapit miedzy linijkami. Ta przerwa jakby mowi Pythonowi, ze kod bedzie tylko wtedy ausgeführt, gdy wartosc jest True
if streckeInKm < 3:
    print("Lauf doch zu Fuß!")
# Tu warunek jest spełniony więc w terminalu wyświetla nam się Lauf doch zu Fuß!

# Teraz tu NIC się nie pokazuje, bo warunek NIE jest spełniony
streckeInKm = 5
if streckeInKm < 3:
    print("Lauf doch zu Fuß!")
else:
    print("Nimm das Fahrrad")

# Tu warunek nie jest spełniony, ale dopisaliśmy else, że jeśli jest False, to wyświetla mu się polecenie żeby wziął rower
streckeInKm = 5
if streckeInKm < 3:
    print("Lauf doch zu Fuß!")
else:
    print("Nimm das Fahrrad")

# Może być jeszcze inna opcja, którą byśmy chcieli dodać, takie jakby inne else.
# Nazywa się elif i MUSI stać międzi if, a else

# Otrzymujemy Die Strecke ist lang. Nimm die Laufschuhe mit!
streckeInKm = 3
if streckeInKm < 3:
    print("Lauf doch zu Fuß!")
elif streckeInKm == 3:
    print("Die Strecke ist lang.")
    print("Nimm die Laufschuhe mit!")
else:
    print("Nimm das Fahrrad")

# Projekt Kinotickets

# int dlatego zeby powstala liczba. Mamy tu 3 opcje: seniorzy, dorosli i dzieci.
# 1 warunek - osoby powyzej 65. 2 warunek - oosby majace wiecej niz 18, ale mniej niz 65, bo na to juz jest warunek
# 3 warunek - dzieci, do 18 roku zycia. Tu juz nie musimy pisac rowniania, bo kazdy przedzial wiekowy oprocz tego do 18 zostal okreslony, wiec tylko ten zostaje
#Cena dla seniorow to 7.50 Euro

alter = int(input("Wie alt bist du?"))
if > 65:
    print(7.5)
elif alter >= 18:
    print(10)
else:
    print(5)

# Wyswieltanam sie w termunalu pytanie Wie alt bist du? Wpisujei pojawia nam sie cena