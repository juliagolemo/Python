# Python
# Podstawowe typy w Pythonie
| Typ        | Opis                             | Przykład      |
| ---------- | -------------------------------- | ------------- |
| `int`      | Liczby całkowite                 | `x = 5`       |
| `float`    | Liczby zmiennoprzecinkowe        | `y = 3.14`    |
| `str`      | Ciągi znaków                     | `s = "Hello"` |
| `bool`     | Wartości logiczne (`True/False`) | `flag = True` |
| `NoneType` | Brak wartości (`None`)           | `z = None`    |

# Metody dla ciągów znaków (str)
| Metoda    | Działanie                           | Przykład                             |
| --------- | ----------------------------------- | ------------------------------------ |
| `replace` | Zastępuje fragment tekstu           | `"kot".replace("k","p") → 'pot'`     |
| `split`   | Dzieli tekst na listę wg separatora | `"a,b,c".split(",") → ['a','b','c']` |
| `join`    | Łączy elementy listy w ciąg znaków  | `",".join(['a','b']) → 'a,b'`        |

#Listy (list) i ich metody
| Metoda   | Działanie                     | Przykład                           |
| -------- | ----------------------------- | ---------------------------------- |
| `append` | Dodaje jeden element na końcu | `lst = [1]; lst.append(2) → [1,2]` |
| `extend` | Dodaje wiele elementów        | `[1].extend([2,3]) → [1,2,3]`      |
| `sort`   | Sortuje listę w miejscu       | `[3,1,2].sort() → [1,2,3]`         |

# Różnice: lista vs krotka (tuple)
| Cecha       | Lista (`list`)       | Krotka (`tuple`)        |
| ----------- | -------------------- | ----------------------- |
| Mutowalność | ✅ Tak                | ❌ Nie (niemutowalna)    |
| Składnia    | `[1,2,3]`            | `(1,2,3)`               |
| Wydajność   | Wolniejsza           | Szybsza (mniej pamięci) |
| Użycie      | Gdy dane się zmienią | Stałe, niezmienne dane  |

