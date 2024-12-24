lista_intow = [3, 4, 10, 32, 46, 2, 51, 4, 6]


def find_min(lista_intow: list[int]) -> int:
    # float('inf') to nieskończoność na + (dodatnia)
    min_int = float('inf')

    for liczba in lista_intow:
        if liczba < min_int:
            min_int = liczba

    return min_int


if __name__ == '__main__':
    print(find_min(lista_intow=[3, 4, 10, 32, 46, 2, 51, 4, 6]))

# 1. pisze funkcje, ktora ma zwrocic z listy intow najmniejszy element
# 2. okreslam czym jest taki element (czyli liczba nieskonczona dodatnia -> nieskonczona, bo moze byc to teoretycznie kazda)
# 3. Piszemy funkcje for (bo chcemy zeby sprawdzilo nam kazda liczbe, przez kazda przeszlo i zobaczylo czy jest najmniejsza)
# 4. Porownujemy liczby: jesli liczba, ktora teraz sprawdzamy, jest mnijesza niz min_int, aktualizujemy obencna najmniejsza watosc (min_int)
# 5. zwracamy wynik
