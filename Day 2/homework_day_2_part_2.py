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
wysokość_2 = f'''{wysokość_1}{wolne_miejsce}{wysokość_1} \n'''


print("Tak wygląda twój prostokąt: ")
print(f'''+{szerokość}+''')
print(wysokość_2 * wysokość, end='')
#for wysokość_1 in range(wysokość):
 #   print(wysokość_2)
print(f'''+{szerokość}+''')




# 6. Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
# Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.


print("Kalkulator liczb z systemu binarnego na dziesiętny.")
wartość_1 = input("Podaj liczbę w systemie binarnym: ")
wartość_1 = wartość_1[0:6]
#DOPISZ ZE TYLKO 010101
wzór_0 = int(wartość_1[0]) * 2 ** 0
wzór_1 = int(wartość_1[1]) * 2 ** 1
wzór_2 = int(wartość_1[2]) * 2 ** 2
wzór_3 = int(wartość_1[3]) * 2 ** 3
wzór_4 = int(wartość_1[4]) * 2 ** 4
wzór_5 = int(wartość_1[5]) * 2 ** 5
wzór = wzór_0 + wzór_1 + wzór_2 + wzór_3 + wzór_4 + wzór_5
print(f'''Obliczenia: {wartość_1}*2^0 + {wartość_1}*2^1 + {wartość_1}*2^2 + {wartość_1}*2^3 + {wartość_1}*2^4 + {wartość_1}*2^5.''')
print(f'''Twoja liczba w systemie dziesiętnym to {wzór}.''')



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
a = 3
b = 5
c = 7
if liczba_2 % a == 0 and liczba_2 % b == 0 and liczba_2 % c == 0:
    print(f'''Liczba jest podzielna przez {a}, {b} i {c}.''')
elif liczba_2 % a == 0 and liczba_2 % b == 0 and liczba_2 % c != 0:
    print(f'''Liczba jest podzielna przez {a} i {b}.''')
elif liczba_2 % b == 0 and liczba_2 % c == 0 and liczba_2 % a != 0:
    print(f'''Liczba jest podzielna przez {b} i {c}.''')
elif liczba_2 % a == 0 and liczba_2 % c == 0 and liczba_2 % b != 0:
    print(f'''Liczba jest podzielna przez {a} i {c}.''')
elif liczba_2 % a == 0:
    print(f'''Liczba jest podzielna tylko przez {a}.''')
elif liczba_2 % b == 0:
    print(f'''Liczba jest podzielna tylko przez {b}.''')
elif liczba_2 % c == 0:
    print(f'''Liczba jest podzielna tylko przez {c}.''')
else:
    print(f'''Liczba nie jest podzielna przez żadne z tych liczb.''')


# 9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7

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
