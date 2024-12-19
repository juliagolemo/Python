import unser_modul
from math import sqrt

unser_modul.begruessung("Julia")
result = sqrt(16)
print(result)

# W tym pliku używamy modułów.
# Moduł to taki plik, który zawiera funkcje, klasy lub zmienne, które możemy wykorzystać w innych częściach programu.
# Dzięki temu możemy nie pisać ciągle tego samego kodu, tylko go zaimportować.

# import unser_modul: Tutaj importujesz pierwszy plik, czyli ten, który zawiera funkcję begruessung. Dzięki temu możesz używać funkcji z tego pliku w drugim.
# unser_modul.begruessung("Julia"): Wywołujesz funkcję begruessung z modułu unser_modul i przekazujesz jej imię "Julia".
# from math import sqrt: Importujesz funkcję sqrt (pierwiastek kwadratowy) z modułu math. Dzięki temu możesz używać funkcji sqrt, która oblicza pierwiastek kwadratowy z liczby.
# Biblioteka math juz jest wgrana w Pythona wiec nie musimy tworzyc osobnego pliku
# result = sqrt(16): Obliczasz pierwiastek kwadratowy z liczby 16, co daje wynik 4.0.

from math import sqrt
result = sqrt(16)
print(result)
