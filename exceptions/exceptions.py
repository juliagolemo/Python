try:
    ergebnis = 10 / 0
except ZeroDivisionError:
    print("Du darfst nicht durch 0 dividieren!")

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
