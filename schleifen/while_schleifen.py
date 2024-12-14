from random import randint
counter = 0

# "Dopoki warunek petli while jest prawdziwy, powtarza to, co jest w petli"
while counter <= 5:
    print(counter)
    counter += 1
# Kazda kolejna liczba bedzie wieksza o 1. W koncu liczba bedzie wielka niz 5, wiec warunek nie bedzie spelniony i na tym sie zatrzyma


einkaufsliste = []
entscheidung = "yes"

while entscheidung == "yes":
    einkaufsliste.append(input("Was moechtest du deiner Liste hinzufuegen? "))
    entscheidung = input(
        "Moechtest du weitere Artikel hinzufuegen ( yes / no ) ")
    print(einkaufsliste)

# Projekt
einkaufsliste = []
# Artikel hinzufügen
# Aktion -> hinzufügen/entfernen/anzeigen/beenden

# Endlos-schleife mit BREAK (statt Bedingung am Anfang nur while True, läuft endlos)
while True:
    aktion = input(
        "Möchtest du einen Artikel hinzufügen/entfernen oder die Liste anzeigen? (hinzufügen / entfernen / anzeigen / beenden)")

    # hinzufügen
    if aktion == "hinzufügen":
        artikel = input("Welchen Artikel möchtest du hinzufügen? ")
        einkaufsliste.append(artikel)
        print("Artikel wurde hinzugefügt")

    # löschen
    elif aktion == "entfernen":
        artikel = input("Welchen Artikel möchtest du entfernen? ")
        if artikel in einkaufsliste:
            einkaufsliste.remove(artikel)
            print("Artikel wurde gelöscht")
        else:
            print("Den Artikel gibt es nicht!")

    # anzeigen
    elif aktion == "anzeigen":
        print("Deine Einkaufsliste:")
        print(einkaufsliste)
    elif aktion == "beenden":
        print("Einkaufsliste beendet")
        break
    else:
        print("Du musst das schon richtig eingeben.")

print(einkaufsliste)

# Übung
zahl = randint(1, 100)

print("Hey ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.")
while True:
    versuch = int(input("Rate meine Zahl: "))

    if versuch == zahl:
        print("Super, du hast die Zahl erraten!")
        break
    elif versuch < zahl:
        print("Die Zahl ist zu klein")
    else:
        print("Die Zahl ist zu groß")
