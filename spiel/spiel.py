# 1. Spielbrett erstellen
def erstelle_brett():
    brett = []
    for i in range(3):
        zeile = [" ", " ", " "]
        brett.append(zeile)
    return brett

# 2. Spielbrett ausgeben
def drucke_brett(brett):
    for zeile in brett:
        print("|".join(zeile))
        print("------")

# 3. Zug machen
def mache_zug(brett, spieler, zeile, spalte):
    if brett[zeile][spalte] == " ":
        brett[zeile][spalte] = spieler
        return True
    else:
        return False

# 4. Gewinn überprüfen
def pruefe_gewonnen(brett, spieler):
    for zeile in range(3):
        if brett[zeile][0] == brett[zeile][1] == brett[zeile][2] == spieler:
            return True

    for spalte in range(3):
        if brett[0][spalte] == brett[1][spalte] == brett[2][spalte] == spieler:
            return True

    if brett[0][0] == brett[1][1] == brett[2][2] == spieler or \
       brett[0][2] == brett[1][1] == brett[2][0] == spieler:
        return True

# 5. Pruefe ob unentschieden
def pruefe_unentschieden(brett):
    for zeile in brett:
        if " " in zeile:
            return False
        return True

# 6. Unsere main

def spiele_tic_tac_toe():
    brett = erstelle_brett()
    aktueller_spieler = "X"

    while True:
        drucke_brett(brett)
        while True:
            try:
                zeile = int(input(f"Spieler {aktueller_spieler}, wähle eine Zeile (0-2): "))
                spalte = int(input(f"Spieler {aktueller_spieler}, wähle eine Spalte (0-2): "))
                break
            except ValueError:
                print("Bitte gib eine gültige Zahl (0-2) ein!")

        if not mache_zug(brett, aktueller_spieler, zeile, spalte):
            print("Ungültig, versuche es erneut!")
            continue
        if pruefe_gewonnen(brett, aktueller_spieler):
            drucke_brett(brett)
            print(f"Du hast gewonnen, {aktueller_spieler}")
            break
        elif pruefe_unentschieden(brett):
            drucke_brett(brett)
            print("Unentschieden")
            break

        aktueller_spieler = "O" if aktueller_spieler == "X" else "X"

spiele_tic_tac_toe()


# range() beschreibt eine Zaehlsequenz bis zum angegebenem Argument
# um eine Codezeile auf 2 dargestellte Teilen umzubrechen, wird ein Backlash (\) gesetzt


