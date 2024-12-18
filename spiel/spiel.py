# Kolko i krzyzyk
# 1. Spielbrett erstellen
def erstelle_brett():
    brett = []
    for i in range(3):
        zeile = [" ", " ", " "]
        brett.append(zeile)
    print(brett)
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

def spiele_tic_tac_toe():
    brett = erstelle_brett
    aktueller_spieler = "X"

    while True:
        drucke_brett(brett)
        zeile = int(input(f"Spieler {aktueller_spieler}, wähle eine Zeile (0-2)"))
        spalte = int(input(f"Spieler {aktueller_spieler}, wähle eine Spalte (0-2)"))

spiele_tic_tac_toe






# range() beschreibt eine Zaehlsequenz bis zum angegebenem Argument



