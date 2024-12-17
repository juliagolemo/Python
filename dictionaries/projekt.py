telefonbuch = {
    "Olivia": "742208714101047",
    "Anna": "742208334101047",
    "Thomas": "742208714101047",
    "Mike": "74220874101047",
}
print("Annas Telefonnummer ist", telefonbuch["Anna"])

a = input("Welche Telefonnummer brauchst du?")
if a in telefonbuch:
    print(a, "Telefonnummer ist", telefonbuch["Anna"])
else:
    print(a, "ist nicht im Telefonbuch")

del telefonbuch[a]
print(a, "wurde gelöscht.")
