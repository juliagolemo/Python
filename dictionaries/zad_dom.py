# Chcemy pobrać pewna listę z API ale te API nie pozwala na zwracanie listy dłuższej niż 5 elementów
# Zadanie polega na tym żeby zawsze móc pobrać całą listę zwirzątek

from typing import Any

# Symulacja bazy danych, która działa jako źródło danych dla naszego API
database_api = {
    1: ["lew", "tygrys", "słoń", "żółw", "koala"],
    2: ["wilk", "lis", "zając", "jelen", "niedźwiedź"],
    3: ["orzeł", "sokół", "kruk", "papuga", "pingwin"],
    4: ["pies", "kot", "świnka morska", "chomik", "papuga"],
    5: ["delfin", "rekin", "ośmiornica", "meduza", "krewetka"]
}


def get_request_api(batch_id: int) -> dict[str, Any]:
    """
    Pobiera dane z `database_api` na podstawie identyfikatora partii (batch_id).

    Args:
        batch_id (int): Identyfikator partii do pobrania.

    Returns:
        dict[str, Any]: Słownik z kluczami:
            - `batch`: Lista zwierząt z danej partii lub `None`, jeśli partia nie istnieje.
            - `next`: Identyfikator następnej partii lub `None`, jeśli to ostatnia partia.

    Przykład:
        >>> get_request_api(1)
        {'batch': ["lew", "tygrys", "słoń", "żółw", "koala"], 'next': 2}
        >>> get_request_api(5)
        {'batch': ["delfin", "rekin", "ośmiornica", "meduza", "krewetka"], 'next': None}
    """
    batch = database_api.get(batch_id)
    next_bach_id = batch_id + 1 if batch_id + 1 in database_api.keys() else None
    return {
        'batch': batch,
        'next': next_bach_id
    }


def fetch_all_animals() -> list[str]:
    """
    Pobiera pełną listę zwierząt korzystając z ograniczonego API.

    Funkcja iteracyjnie pobiera partie danych, aż do momentu, gdy żadna kolejna partia
    nie będzie dostępna. Łączy wszystkie wyniki w jedną listę.

    Returns:
        list[str]: Pełna lista wszystkich zwierząt.

    Przykład:
        >>> fetch_all_animals()
        ["lew", "tygrys", "słoń", "żółw", "koala", "wilk", "lis", ...]
    """
    all_animals = []

    batch_id = 1

    while batch_id:
        print("batch", batch_id)
        data = get_request_api(batch_id)
        print("Moje dane:", data)
        # trzeba jakoś zatrzymać tą pętle zmieniajac batch_id w tej pętli na np. None
        # batch_id = ...

    return all_animals

# Batch to porcja danych, będąca częścią większej listy,
# podzielonej na mniejsze grupy w celu bardziej efektywnego przetwarzania.
# Cała lista może składać się z wielu batchy, co umożliwia równoczesną pracę nad różnymi
# fragmentami danych lub wykonywanie operacji w sposób uporządkowany i zoptymalizowany.


if __name__ == '__main__':
    # Wywołanie funkcji i wyświetlenie pełnej listy zwierząt
    animals = fetch_all_animals()
    print("Pełna lista zwierząt:", animals)
