# Leere Liste - to jest taki jakby nasz koszyk na zalupach, ktory najpierw jest pusty
leere_liste = []
print(leere_liste)

# Wartości(itemy) listy liczymy od 0
einkaufszettel = ["Bananen" , "Weintrauben", "Schockolade"]
print(einkaufszettel)
# wyswietla nam sie wszystko

print(einkaufszettel[2])
# Wyswietla nam sie tylko Schockolade
print(einkaufszettel[0])
print(einkaufszettel[1])

# określanie typu, czym jest Schockolade itd
print(type(einkaufszettel[2]))
print(type(einkaufszettel[2][1]))
print(type(einkaufszettel[-1]))

# Funktionen fuer Listen
# Funkcja Append pozwala na dodawanie elementow, dodaje je na koniec listy
einkaufszettel.append("Milch")
print(einkaufszettel)

# Funktion insert
#Teraz chcemy cos dodac, ale z przodu
einkaufszettel.insert(0, "Wasser")
print(einkaufszettel)

# Tu chcemy dać chleb na 2 miejscu
einkaufszettel.insert(2, "Brot")
print(einkaufszettel)

# Funktion remove
# Teraz chcemy usunąć jakiś produkt
einkaufszettel.remove("Schockolade")
print(einkaufszettel)
einkaufszettel.remove("Wasser")
print(einkaufszettel)
einkaufszettel.insert(0, "Wasser")
print(einkaufszettel)

# Funktion pop - usuwa ostatni element. 
# Nawias może zostać pusty, bo i tak zawsze chodzi o ostatni element
einkaufszettel.pop()
print(einkaufszettel)

# Funktion del (delete)
# Chcemy usunąć pierwszy element, lub którykolwiek
del einkaufszettel[0]
print(einkaufszettel)
del einkaufszettel[2]
print(einkaufszettel)

# Funktion len
print(len(einkaufszettel))
print(einkaufszettel)

# Funktion max, przy liczbach to ma wiecej sensu xd
print(max(einkaufszettel))

# Funktion min
print(min(einkaufszettel))

einkaufszettel.insert(0, "Wasser")
print(einkaufszettel)

# Chce zeby wyswietlal mi sie tylko 1 element i 2. Pamietac zeby zawsze przy koncu podawac numer wiecej!
print(einkaufszettel[1:2])
print(einkaufszettel[1:len(einkaufszettel)])


# Zagniezdzone listy, lista w liscie
einkaufszettel = ["Bananen" , "Weintrauben", "Schockolade" , ["Gurken" , "Tomaten"]]
print(einkaufszettel)

# Wyswietli sie tylko 2 element
einkaufszettel = ["Bananen" , "Weintrauben", "Schockolade" , ["Gurken" , "Tomaten"]]
print(einkaufszettel[2])

einkaufszettel = ["Bananen" , "Weintrauben", "Schockolade" , ["Gurken" , "Tomaten"]]
print(einkaufszettel[1][0][1:4])
