from moduly.calculators import calculatorCtoF, calculatorFtoC, pole_kola
from moduly.calculators import rokprzestepny
from moduly.numbers import pierwsza_ostatnia_cyfra, parzysta, podzielnaprzez3lub5lub7, podzielnaprzez3i5i7
from moduly.drawnings import rectangle
from moduly.binarne import binarytodecimal

# 1. Program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)
# wzór °F = (°C × 1.8) + 32

calculatorCtoF()

# 2. Program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
# wzór = (°F − 32)/1.8

calculatorFtoC()

# 3. Program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
# wzór  π r²

pole_kola()

# 4. Program, który podaje pierwszą i ostatnią cyfrę podanej liczby


pierwsza_ostatnia_cyfra()


# 5. Program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
#     | (bok)
#     - (góra/dół)
#     + (wierzchołek)
#     czyli np:
#     +-------+
#     |       |
#     |       |
#     +-------+

rectangle()


# 6. Program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
# Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.

binarytodecimal()

# 7. Program do rozpoznawania czy podana liczba jest parzysta czy nie.

parzysta()

# 8. Program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7


podzielnaprzez3lub5lub7()


# 9. Program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7


podzielnaprzez3i5i7()


# 10. Program do sprawdzania czy podany rok jest rokiem przestępnym


rokprzestepny()








