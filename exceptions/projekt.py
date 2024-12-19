x = 10
raise Exception("Sorry, X darf nicht gleich oder größer 10 sein!")

# mit raise Exception("...") kannst du eigene Fehlermeldungen definieren
# raise służy do rzucenia wyjątku
#  Wyjątek to specjalny mechanizm w Pythonie, który przerywa działanie programu, gdy napotka błąd
# Exception to wbudowana klasa w Pythonie, która reprezentuje ogólny błąd.
# Możesz przekazać wiadomość (w tym przypadku: "Sorry, X darf nicht gleich oder größer 10 sein!"), która zostanie wyświetlona, gdy wyjątek zostanie zgłoszony.
# Ponieważ instrukcja raise Exception(...) znajduje się w kodzie, program natychmiast przerywa działanie, gdy tylko napotka tę linię. 
