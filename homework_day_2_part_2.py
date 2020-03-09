# 5. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
#     | (bok)
#     - (góra/dół)
#     + (wierzchołek)
#     czyli np:
#     +-------+
#     |       |
#     |       |
#     +-------+

print('Narysuj prostokąt o określonym rozmiarze.')
wysokość = input('Podaj wysokość prostokąta: ')
szerokość = input('Podaj szerokość prostokąta: ')
wysokość = int(wysokość)
szerokość = int(szerokość)

wolne_miejsce = ' ' * szerokość
szerokość = "-" * szerokość
wysokość_1 = "|"
wysokość_2 = f'''{wysokość_1}{wolne_miejsce}{wysokość_1}'''


print("Tak wygląda twój prostokąt: ")
print(f'''+{szerokość}+''')
for wysokość_1 in range(wysokość):
    print(wysokość_2)
print(f'''+{szerokość}+''')





# 7. Napisz program do rozpoznawania czy podana liczba jest parzysta czy nie.

print("Sprawdź czy dana liczba jest parzysta.")
liczba_1 = input("Podaj liczbę: ")
liczba_1 = int(liczba_1)
if liczba_1 % 2 == 0:
    print("Liczba jest parzysta.")
else:
    print("Liczba jest nieparzysta.")

# 8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7

print("Sprawdź czy dana liczba jest podzielna przez 3 lub 5 lub 7.")
liczba_2 = input("Podaj liczbę: ")
liczba_2 = int(liczba_2)
if liczba_2 % 3 == 0:
    print("Liczba jest podzielna przez 3.")
else:
    print("Liczba nie jest podzielna przez 3.")
if liczba_2 % 5 == 0:
    print("Liczba jest podzielna przez 5.")
else:
    print("Liczba nie jest podzielna przez 5.")
if liczba_2 % 7 == 0:
    print("Liczba jest podzielna przez 7.")
else:
    print("Liczba nie jest podzielna przez 7.")

# 9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7\

print("Sprawdź czy dana liczba jest podzielna przez 3 i 5 i 7.")
liczba_3 = input("Podaj liczbę: ")
liczba_3 = int(liczba_3)
if liczba_3 % 3 == 0 and liczba_3 % 5 == 0 and liczba_3 % 7 == 0:
    print("Liczba jest podzielna przez 3 i 5 i 7.")
else:
    print("Liczba nie jest podzielna przez 3 i 5 i 7.")
#105

# 10. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym

print("Sprawdź czy podany rok jest rokiem przestępnym. ")
data = input("Podaj datę: ")
data = int(data)
if data % 4 == 0 and data % 100 != 0 or data % 400 == 0:
    print("Podany rok jest rokiem przestępnym.")
else:
    print("Podany rok nie jest rokiem przestępnym.")
