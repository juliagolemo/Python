# For Schleifen (benutzt um über Sequenzen (z.B. String, Liste, Tupel) mehrfach zu interieren)


liste = ["Banane", "Weintrauben", "Nüsse"]

# dla kazdego elementu po kolei w liscie zrob to i to.
# Kiedy np. lista sie skonczy, nie musimy tak jak w while przerywac petli, tu sie sama zatrzyma
# ten "element" nie musi sie tak nazywac, mozemy go nazwac jak chcemy
for element in liste:
    print(element)
# wyswietlily nam sie wszytskie produkty

name = "Julia"
for i in name:
    print(i)
# Wyswietli nam po kolei litery imienia


liste = [1500, 1000, 3000, 5000, 200]
bezahlbare = []
for i in liste:
    if i <= 1000:
        bezahlbare.append(i)
    else:
        print(str(i) + "ist zu teuer!")
print(bezahlbare)



