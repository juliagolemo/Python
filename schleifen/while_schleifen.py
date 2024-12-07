counter = 0

# "Dopoki warunek petli while juest prawdziwy, powtarza to, co jest w petli"
while counter <= 5:
    print(counter)
    counter += 1
# Kazda kolejna liczba bedzie wieksza o 1. W koncu liczba bedzie wielka niz 5, wiec warunek nie bedzie spelniony i na tym sie zatrzyma


einkaufsliste = []
entscheidung = "yes"

while entscheidung == "yes":
    einkaufsliste.append(input("Was moechtest du deiner Liste hinzufuegen? "))
    entscheidung = input("Moechtest du weitere Artikel hinzufuegen ( yes / no ) ")

# tbc
    