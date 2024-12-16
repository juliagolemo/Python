# Dictionaries (Schnellzugriff)
# Schlüssel müssen individuell sein

leeres_dict = {}

einkauft_dickt = {
    "artikelname": "Banane",
    "Preis": 2,
    "Ablaufdatum": 2024,
    "Farbe": ["gelb", "grün"]
}
print(einkauft_dickt)
# Tu po prostu wyswietlamy slownik

# W jaki sposób moge "zajac sie" jakims konkretnym elementem?
# print(einkauft_dickt) ---> print(einkauft_dickt["Preis"])

print(einkauft_dickt["Preis"])
print(einkauft_dickt["Farbe"][0])

# W ten sposob wyswietlam wszystkie "parametry""czyli "name"itd.
print(einkauft_dickt.keys())

# Tak wyswietlamy typ
print(type(einkauft_dickt.keys()))

# A tak wartosci
print(einkauft_dickt.values())

# Zmieniamy Preis na 3
einkauft_dickt["Preis"] = 3
print(einkauft_dickt)

# Zmieniamy preis na 5
einkauft_dickt["Preis"] = 5
print(einkauft_dickt)

# W ten sposob dodalismt jeszcze Gewicht
einkauft_dickt["Gewicht"] = 10

# Tak usuwamy Ablaufdatum
einkauft_dickt.pop("Ablaufdatum")
print(einkauft_dickt)




julia_dickt = {
    "name": "Julia",
    "Alter": 23,
}
print(julia_dickt)
