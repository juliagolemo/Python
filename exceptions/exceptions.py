try:
    ergebnis = 10 / 0
except ZeroDivisionError:
    print("Du darfst nicht durch 0 dividieren!")

# try oznacza: "Spróbuj wykonać ten kod"
# W środku jest 10 / 0, czyli próbujemy podzielić 10 przez 0. To powoduje błąd podziału przez zero
# Kiedy taki błąd wystąpi, program przechodzi do sekcji except ZeroDivisionError:
# W tej sekcji program wypisuje: "Du darfst nicht durch 0 dividieren!"


try:
    ergebnis = 10 / 2
except ZeroDivisionError:
    print("Du darfst nicht durch 0 dividieren!")
except TypeError:
    print("Du kannst nur mit zahlen rechnen!")
except:
    print("Hier ist etwas schief gegangen.")
else:
    print("Kein Fehler, super!")

# try: Program próbuje podzielić 10 / 2, co jest ok
# Sekcja except jest jak zestaw różnych "pułapek" na błędy:
# except ZeroDivisionError: Gdyby był błąd dzielenia przez zero (ale go tutaj nie ma)
# except TypeError: Gdyby był błąd typu (np. próbowalibyśmy dzielić liczbę przez tekst – ale tutaj tego nie ma).
# except: To taki "łapacz na wszystko inne". Gdyby coś innego poszło źle
# Ale ponieważ dzielenie 10 / 2 działa poprawnie, żadna z sekcji except się nie uruchamia.
# Zamiast tego wchodzi do else, co oznacza: "Kein Fehler, super!"

try:
    ergebnis = 10 / 2
except ZeroDivisionError:
    print("Du darfst nicht durch 0 dividieren!")
except TypeError:
    print("Du kannst nur mit zahlen rechnen!")
except:
    print("Hier ist etwas schief gegangen.")
finally:
    print("Alles ist durchgelaufen!")

# Nowość: Jest blok finally. To oznacza: "Wykonaj ten kod zawsze, niezależnie od tego, czy był błąd, czy go nie było."
# Dlatego nawet jeśli dzielenie zadziałało poprawnie, program wypisuje: "Alles ist durchgelaufen!", czyli "Wszystko zostało zakończone!".
# Jeśli wszystko jest OK, wyswietla finally.
# Jesli cos jest nie tak, wyswietla np. "Du darfst nicht durch 0 dividieren!" i DODATKOWO finally
# FINALLY WYSWIETLA ZAWSZE -  niezależnie od tego, czy był błąd, czy nie
