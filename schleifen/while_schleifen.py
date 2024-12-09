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
    print(einkaufsliste)

# Projekt
einkaufsliste = []
# Artikel hinzufügen
# Aktion -> hinzufügen/entfernen/anzeigen/beenden

# Endlos-schleife mit BREAK (statt Bedingung am Anfang nur while True, läuft endlos)
while True:
    aktion = input("Möchtest du einen Artikel hinzufügen/entfernen oder die Liste anzeigen? (hinzufügen / entfernen / anzeigen / beenden)")

    # hinzufügen
    if aktion == "hinzufügen":
        atikel = input("Welchen Artikel möchtest du hinzufügen? ")
        einkaufsliste.append(artikel)
        print("Artikel wurde hinzugefügt")

    # löschen
    elif aktion == "entfernen":
        artikel = input("Welchen Artikel möchtest du hinzufügen? ")
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


2h 30 min




