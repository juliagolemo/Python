# Python
## Podstawowe typy w Pythonie
| Typ        | Opis                             | Przykład      |
| ---------- | -------------------------------- | ------------- |
| `int`      | Liczby całkowite                 | `x = 5`       |
| `float`    | Liczby zmiennoprzecinkowe        | `y = 3.14`    |
| `str`      | Ciągi znaków                     | `s = "Hello"` |
| `bool`     | Wartości logiczne (`True/False`) | `flag = True` |
| `NoneType` | Brak wartości (`None`)           | `z = None`    |

## Metody dla ciągów znaków (str)
| Metoda    | Działanie                           | Przykład                             |
| --------- | ----------------------------------- | ------------------------------------ |
| `replace` | Zastępuje fragment tekstu           | `"kot".replace("k","p") → 'pot'`     |
| `split`   | Dzieli tekst na listę wg separatora | `"a,b,c".split(",") → ['a','b','c']` |
| `join`    | Łączy elementy listy w ciąg znaków  | `",".join(['a','b']) → 'a,b'`        |

## Listy (list) i ich metody
| Metoda   | Działanie                     | Przykład                           |
| -------- | ----------------------------- | ---------------------------------- |
| `append` | Dodaje jeden element na końcu | `lst = [1]; lst.append(2) → [1,2]` |
| `extend` | Dodaje wiele elementów        | `[1].extend([2,3]) → [1,2,3]`      |
| `sort`   | Sortuje listę w miejscu       | `[3,1,2].sort() → [1,2,3]`         |

## Różnice: lista vs krotka (tuple)
| Cecha       | Lista (`list`)       | Krotka (`tuple`)        |
| ----------- | -------------------- | ----------------------- |
| Mutowalność | ✅ Tak                | ❌ Nie (niemutowalna)    |
| Składnia    | `[1,2,3]`            | `(1,2,3)`               |
| Wydajność   | Wolniejsza           | Szybsza (mniej pamięci) |
| Użycie      | Gdy dane się zmienią | Stałe, niezmienne dane  |

# Słowniki (dict)
## klucz → wartość
```python
osoba = {"imię": "Anna", "wiek": 25}
print(osoba["imię"])  # Anna
```
## Podstawowe metody słowników
get - pobieranie wartości

items() – zwraca pary (klucz, wartość)
## Inne przydatne metody:
keys() – zwraca listę kluczy

values() – zwraca listę wartości

update() – aktualizuje słownik innym słownikiem

pop(key) – usuwa element o danym kluczu

# Zbiory (set)

Zbiór przechowuje unikalne elementy (duplikaty są automatycznie usuwane)

Operacje union: (łączy elementy), intersection: (elementy wspólne)

# Moduły i funkcje
import x – importuje cały moduł

from x import y – importuje konkretną funkcję/zmienną

# Docstringi
Pierwszy napis (w cudzysłowie potrójnym) w funkcji, klasie lub module.
Służy do dokumentowania działania kodu.

```python
def dodaj(a, b):
    """Zwraca sumę dwóch liczb a i b."""
    return a + b

# Ułatwiają zrozumienie kodu innym programistom (i sobie w przyszłości)

