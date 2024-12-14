# Program losujący liczby w pętli while
# 1. Wylosuj liczby całkowite z przedzioału 1900-2025 za pomocą funkcji randint() z biblioteki random.
# 2. Pętla powinna działać dopóki wylosowana liczba nie będzie równa 1920.
# 3. Każda wylosowana liczba powinna zostać wypisana na ekranie.
# 4. Gdy wylosowana zostanie liczba 1920, również wypisz "Ino Ruch!!!", a następnie zakończ działanie programu.

# Przykład użycia funkcji randint() znajduje się tutaj:
# https://www.w3schools.com/python/ref_random_randint.asp

import random

while True:
    liczba = random.randint(1900, 2025)
    print(liczba)

    if liczba == 1920:
        print("Ino Ruch!!!")
        break


