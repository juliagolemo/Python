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