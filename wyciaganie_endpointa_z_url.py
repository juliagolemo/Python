def wyciaganie_endpointa_z_url(url):
    """
    Wyjaśnienie działania query params w URL:
    ----------------------------------------
    Query parameters to dodatkowe informacje w URL, które umożliwiają filtrowanie lub przekazywanie danych do endpointu.
    W URL występują po znaku `?`, a kolejne parametry oddzielone są symbolem `&`. Każdy parametr ma postać klucz=wartość.

    Przykład struktury URL z query params:
    http://nazwa-strony/sciezka/endpoint?queryparam=wartosc_query_param

    Struktura URL:
    - http://            -> protokół
    - nazwa-strony       -> nazwa domeny (host)
    - /sciezka/endpoint  -> ścieżka, kończąca się na endpoint (ostatni segment ścieżki)
    - ?queryparam=...    -> query parameters, czyli parametry zapytania

    W powyższym przykładzie:
    - `endpoint` to końcowy segment ścieżki URL.
    - `queryparam=wartosc_query_param` to query parameter, gdzie `queryparam` jest kluczem, a `wartosc_query_param` jest wartością.

    Przykłady różnic między URL bez i z query params:
    a) URL bez query params:
      http://sklep/napoje/piwa

      Wynik zapytania: lista wszystkich piw:
      [
          {'marka': 'żywiec', 'cena': '4'},
          {'marka': 'tyskie', 'cena': '3'},
          {'marka': 'miłoslaw', 'cena': '5'}
      ]

    b) URL z query params (filtrujemy listę po parametrze `marka`):
      http://sklep/napoje/piwa?marka=tyskie

      Wynik zapytania:
      {'marka': 'tyskie', 'cena': '3'}

    Cel funkcji:
    ------------
    Funkcja służy do wyodrębnienia *endpointu* z URL, czyli ostatniego segmentu ścieżki przed znakiem `?` (jeśli występuje) lub końcem URL.
    Endpoint to kluczowa część URL, określająca zasób, na który kierowane jest zapytanie.

    Przykłady użycia:
    -----------------
    1) http://sklep/napoje/piwa?marka=tyskie -> "piwa"
    2) https://www.youtube.com/results?search_query=python+ui+deutsch -> "results"
    3) https://www.google.com/search/cos/ktos?e232131 -> "ktos"
    4) https://www.google.com/search?client=firefox-b-d&q=dada -> "search"

    Parametry wejściowe:
    --------------------
    url : str
       URL, z którego chcemy wyodrębnić endpoint.

    Zwraca:
    -------
    str
       Ostatni segment ścieżki URL, czyli nazwę endpointu, bez parametrów zapytania.
    """
    split_url = url.split('/')
    print(f'{split_url=}')
    ostatni_element_url = split_url[-1]
    print(f'{ostatni_element_url=}')
    split_ostatni_element_url = ostatni_element_url.split('?')
    print(f'{split_ostatni_element_url=}')
    nazwa_endpointa = split_ostatni_element_url[0]
    print(f'{nazwa_endpointa=}')
    return nazwa_endpointa


if __name__ == '__main__':
    url = 'https://www.youtube.com/results?search_query=python+auif+deutch'
    print(wyciaganie_endpointa_z_url(url=url))
