#=========================================Slicing==================================================
# 
# sequence[start:stop:step]
# 
# start - indeks, od którego zaczynamy wycinanie (włącznie). Domyślnie 0.
# stop - indeks, na którym kończymy wycinanie (ale go nie uwzględniamy). Domyślnie długość sekwencji.
# step - krok, z jakim wybieramy elementy. Domyślnie 1.



def drop_n_th_element(s: str, n: int) -> str:
    """
    Usuwa n-ty element z podanego ciągu znaków.

    Funkcja przyjmuje ciąg znaków `s` oraz indeks `n` (liczony od 0)
    i zwraca nowy ciąg znaków, w którym n-ty element został pominięty.
    Jeśli `n` jest poza zakresem indeksów ciągu, zwraca oryginalny ciąg.

    Parametry:
        s (str): Ciąg znaków, z którego ma zostać usunięty element.
        n (int): Indeks elementu do usunięcia (liczony od 0).

    Zwraca:
        str: Nowy ciąg znaków z pominięciem n-tego elementu.
    """
    return s[:n] + s[n+1:]


def reverse_string(s: str) -> str:
    """
    Odwraca podany ciąg znaków.

    Funkcja przyjmuje ciąg znaków `s` i zwraca nowy ciąg znaków,
    w którym kolejność wszystkich znaków została odwrócona.

    Parametry:
        s (str): Ciąg znaków, który ma zostać odwrócony.

    Zwraca:
        str: Nowy ciąg znaków z odwróconą kolejnością znaków.

    Przykłady:
        >>> reverse_string("abcdef")
        'fedcba'
        >>> reverse_string("12345")
        '54321'
        >>> reverse_string("")
        ''
    """
    return s[::-1]

def get_last_element(s: str) -> str:
    """Zwraca ostatni element ciągu"""
    return s[-1]

def get_last_n_elements(s: str, n: int) -> str:
    """Zwraca ostatnie n znaków z ciągu."""
    return s[-n:]

def extract_every_third_character(s: str) -> str:
    """
    Zwraca co trzeci znak z podanego ciągu znaków.

    Parametry:
        s (str): Ciąg wejściowy.

    Zwraca:
        str: Nowy ciąg zawierający co trzeci znak z ciągu wejściowego.
    """
    return s[2::3]  # Zaczyna od trzeciego znaku (indeks 2 bo od 0 liczymy) i wybiera co trzeci znak.

if __name__ == '__main__':
    print(drop_n_th_element('usun mnie', 4))
    print(reverse_string('odwróć mnie'))