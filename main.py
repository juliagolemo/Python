# funkcja ktora przyjmuijue tablice liczb i ma wewnatrz siebieb fu7nkcje (tzw inner funkcje, ktoraw przyjmuje argument int i sprawedza czy ta liczba jest parzysta czy niue) Fun kacja glowna ma przejsc przez wszystkie liczbuy i uzxyc. funkcji wewnetrznej zeby wypisac te parzyste


def liczby(tablica: list[int]) -> None:
    def is_even(liczba: int) -> bool:
        """
        prametry `liczba` to parametr jest intem

        zwraca czy liczba jest parzysta
        """
        if liczba % 2 == 0:
            return True
        else:
            return False
        
    for liczba in tablica:
        if is_even(liczba):
            print(liczba)
            
liczby([1, 2, 3, 4, 5, 6])