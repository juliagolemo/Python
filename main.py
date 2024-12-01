print('Hallo Welt!')
print("Ich habe Hallo Welt programmiert")

# Variable 
x = 5
# Wyświetla się nam 5
print(x)

# Wyświetla się nam x 
print("x")

# Bei Variabeln geben wir ZUERST x, dann print(...)

# Um etwas einzuschalten, geben wir "pyhon main.py" ein

# Uebung 1
firmenname = "Lufthansa"
print("Hallo liebes Team von " + firmenname + " ,ich moechte gerne mit euch in der Firma " + firmenname + " arbeiten.")

# Uebung 2 - fuege einen zweiten Aufgabebefehl mit der Variable berufsfeld hinzu, der zu deinen Wunschberuf zuweist.
firmenname = "Lufthansa"
berufsfeld = "Junior HR Advisor"
weiterbildungsdauer = "2"
print("Ich habe einen Weiterbildung zum " + berufsfeld + "gemacht. ")
print(weiterbildungsdauer)

# Pisząc weiterbildungsdauer = 2, wyświetli się nam 2
# Pisząc weiterbildungsdauer = 2 - 1, wyświetli się nam 1
# Pisząc "2 - 1", wyświetli się nam "2 - 1"

# Einfache Datentypen: string, int, float, bool

#string - mając np. napisz Hallo Welt, możemy do każdej litery przypasować liczbę. ZAWSZE zaczynami od 0, a pauzy również są wliczane (litera H będzie miała numer 0)

# Wyświetli się nam napis Hallo Welt
x = 'Hallo Welt'
print(x)

# Wyświetli się nam tylko litera W, bo jest 6 w kolejności
x = 'Hallo Welt'
print(x[6])

# Wyświetli się nam litera t, bo liczymy od końca (-1)
x = 'Hallo Welt'
print(x[-1])

# Wyświetli się nam litera l, bo liczymy od końca (-2)
x = 'Hallo Welt'
print(x[-2])

#SLICING - Konzept zum Zerlegen von Sequenzen/Strings anhand ihrer Indizes. Ermoeglich z.B. Isolieren einzelnen Woerter

# Uebung 1 - Chcę "wyciągnąć" słowo Welt z 'Hallo Welt'
# Piszę 6, bo od 6 zaczyna się to słowo
# Po : piszemy liczbę, do którego miejsca chcemy wyciągnąć słowo. Jeśli nie damy nic, automatycznie wyciągnie nam wszystko do końca
x = 'Hallo Welt'
print(x[6:]) 


# Uebung 2 - Chcę "wyciągnąć" słowo Hallo z 'Hallo Welt'
# Jeśli chcemy zacząc od samego początku, nie musimy podawać przed : liczby. Python automatycznie zacznie od 0.
# Na 5 chcemy skończyć
x = 'Hallo Welt'
print(x[:5]) 

# FUNKTION len() - einfache Funktion zum Zaelen der Bestandteile eines Objekts
#zawsze używamy do tego print. W "srodkowym nawiasie, piszemy CO checmy policzyć"
y = "Dieser Satz ist recht lang. Wie lang ist er?"
print(len(y))

# wir koennen das auch so machen
# WICHTIG: Strings werden mit + verkettet, Elemente verschiedener Datentypen mit Komma

print("Der String mit der Variable y ist", len(y), "Zeichen lang.")

# Wie kann man bei Strings Buchstaben veraendern?
# Jest problematycznie, gdzie chcemy zmienić dużą literę na małą i na odwrót
# Chcemy to H połączyć z dalszą częścią stringa. CZĘŚCIĄ. Dlatego dajemy x[]
x= "hallo"

x = "H" + x[1:]
# 1 dlatego, bo "a" ma liczbę 1(bo zaczynamy od 0)
# po : nie piszemy nic, bo jedziemy do końca
print(x)
# CHCEMY WYŚWIETLIĆ HALLO 10 RAZY
# 1 sposób -> po prostu wypisanie
# lub

x = "Hallo"
print(x + x + x + x + x + x + x + x + x + x)

# lub
x = "Hallo"
print(x * 10)


# FUNKTIONEN FUER STRINGS

# U.1 Chcemy żeby wszystko było dużymy literami

x = "Hallo Welt"
print(x.upper())

#JAK CHCEMY małymi -> lower
x = "Hallo Welt"
print(x.lower())

# U.2 Chcemy rozdzielić słowa SPLIT (wyjdzie nam: ['Hallo', 'Welt'])
x = "Hallo Welt"
print(x.split())

# Teraz chcemy rozdzielić zdanie, lecz nie na poszczególne słowa, lecz części. Chcemy otrzymać: ['Hallo Welt', ' ich lerne Python']
# W nawiasie podajemy, GDZIE chcemy podzielić zdanie. Jeśli nawias byłby pusty, rodzieliłoby nam każde słowo
x = "Hallo Welt, ich lerne Python"
print(x.split(","))
