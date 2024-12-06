def is_palindrome(s: str) -> bool:
    """
    Sprawdza, czy podany ciąg znaków jest palindromem.

    Palindrom to ciąg znaków, który czytany od lewej do prawej
    i od prawej do lewej jest taki sam.

    Args:
        s (str): Ciąg znaków do sprawdzenia.

    Returns:
        bool: True, jeśli ciąg znaków jest palindromem, w przeciwnym razie False.

    Przykład:
        >>> is_palindrome("kajak")
        True
        >>> is_palindrome("python")
        False
        >>> is_palindrome("AmanaplanacanalPanama")
        True
    """
    odwrocony_pomniejszony = s[::-1].lower()
    pomniejszony_oryginal = s.lower()
    return pomniejszony_oryginal == odwrocony_pomniejszony
    

def test_is_palindrome():
    """
    Testuje funkcję is_palindrome za pomocą zestawu przypadków testowych.
    Dla każdego testu sprawdza, czy wynik funkcji zgadza się z oczekiwanym rezultatem.

    Wypisuje "Test X pass" w przypadku sukcesu, a w przypadku błędu szczegóły różnicy.
    """
    test_cases = [
        ("kajak", True),
        ("python", False),
        ("AmanaplanacanalPanama", True),
        ("12321", True),
        ("12345", False),
        ("", True),
        ("a", True),
    ]

    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = is_palindrome(input_str)
        if result == expected:
            print(f"Test {i} pass")
        else:
            print(f"Test {i} fail: input({input_str}) => expected({expected}), got({result})")


if __name__ == "__main__":
    test_is_palindrome()
