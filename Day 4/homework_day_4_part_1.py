# 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)
# wzór °F = (°C × 1.8) + 32

def calculatorCtoF(c=input('''Kalkulator °C do °F.
Podaj temperaturę w °C: '''),x=1.8,y=32):
    c = float(c)
    wynik = (c*x)+y
    print(f'Wynik to: {wynik}°F. Dziękujemy za skorzyskanie z kalkulatora.')
calculatorCtoF()


# 2. Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
# wzór = (°F − 32)/1.8

def calculatorFtoC(f=input('''Kalkulator °F do °C.
Podaj temperaturę w °C: '''),x=1.8,y=32):
    f = float(f)
    wynik_1 = (f-y)/x
    print(f'Wynik to: {wynik_1}°C. Dziękujemy za skorzystanie z kalkulatora.')
calculatorFtoC()


# 3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
# wzór  π r²

def pole_kola(π=3.14,r=input('''Kalkulator powierzchni koła. 
Podaj promień [w cm]: ''')):
    r = float(r)
    pole = π*r**2
    print(f'Wynik to: {pole}cm. Dziękujemy za skorzystanie z kalkulatora.')
pole_kola()


# 4. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby

def pierwsza_ostatnia_cyfra(x=input('''Pierwsza i ostatnia cyfra danej liczby:
Podaj dowolną liczbę: ''')):
    pierwsza_cyfra = x[0]
    ostatnia_cyfra = x[-1]
    print(f'Pierwsza cyfra to {pierwsza_cyfra}, a ostatnia cyfra to {ostatnia_cyfra}.')
pierwsza_ostatnia_cyfra()


# 5. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
#     | (bok)
#     - (góra/dół)
#     + (wierzchołek)
#     czyli np:
#     +-------+
#     |       |
#     |       |
#     +-------+

def prostokąt(a = input('''Narysuj prostokąt o określonym rozmiarze.
Podaj wysokość prostokąta: '''),b = input('''
Podaj szerokość prostokąta: ''')):
    a = int(a)
    b = int(b)
    space = ' ' * b
    ściana = '|'
    wysokość = f'''{ściana}{space}{ściana}'''
    szerokość = "-" * b
    print(f'Tak wygląda twój prostokąt: ')
    print(f'+{szerokość}+')
    for ściana in range(a):
        print(wysokość)
    print(f'+{szerokość}+')
prostokąt()


# 6. Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
# Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.

def binarytodecimal(liczba = input('''Kalkulator liczb z systemu binarnego na dziesiętny.
Podaj liczbę w systemie binarnym: ''')):
    liczba = liczba[0:6]
    wzór_0 = int(liczba[0]) * 2 ** 0
    wzór_1 = int(liczba[1]) * 2 ** 1
    wzór_2 = int(liczba[2]) * 2 ** 2
    wzór_3 = int(liczba[3]) * 2 ** 3
    wzór_4 = int(liczba[4]) * 2 ** 4
    wzór_5 = int(liczba[5]) * 2 ** 5
    wzór = wzór_0 + wzór_1 + wzór_2 + wzór_3 + wzór_4 + wzór_5
    print(f'''Obliczenia: {liczba}*2^0 + {liczba}*2^1 + {liczba}*2^2 + {liczba}*2^3 + {liczba}*2^4 + {liczba}*2^5.
Twoja liczba w systemie dziesiętnym to: {wzór}.''')
binarytodecimal()

# 7. Napisz program do rozpoznawania czy podana liczba jest parzysta czy nie.

def parzysta(liczba_1 = input('''Sprawdź czy dana liczba jest parzysta.
Podaj liczbę: ''')):
    liczba_1 = int(liczba_1)
    if liczba_1 % 2 == 0:
        print("Liczba jest parzysta.")
    else:
        print("Liczba jest nieparzysta.")
parzysta()

# 8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7

def podzielnaprzez3lub5lub7(liczba_3 = input('''Sprawdź czy dana liczba jest podzielna przez 3 lub 5 lub 7.
Podaj liczbę: ''')):
    dz1 = 3
    dz2 = 5
    dz3 = 7
    liczba_3 = int(liczba_3)
    if liczba_3 % dz1 == 0 and liczba_3 % dz2 == 0 and liczba_3 % dz3 == 0:
        print(f'''Liczba jest podzielna przez {dz1}, {dz2} i {dz3}.''')
    elif liczba_3 % dz1 == 0 and liczba_3 % dz2 == 0 and liczba_3 % dz3 != 0:
        print(f'''Liczba jest podzielna przez {dz1} i {dz2}.''')
    elif liczba_3 % dz2 == 0 and liczba_3 % dz3 == 0 and liczba_3 % dz1 != 0:
        print(f'''Liczba jest podzielna przez {dz2} i {dz3}.''')
    elif liczba_3 % dz1 == 0 and liczba_3 % dz3 == 0 and liczba_3 % dz2 != 0:
        print(f'''Liczba jest podzielna przez {dz1} i {dz3}.''')
    elif liczba_3 % dz1 == 0:
        print(f'''Liczba jest podzielna tylko przez {dz1}.''')
    elif liczba_3 % dz2 == 0:
        print(f'''Liczba jest podzielna tylko przez {dz2}.''')
    elif liczba_3 % dz3 == 0:
        print(f'''Liczba jest podzielna tylko przez {dz3}.''')
    else:
        print(f'''Liczba nie jest podzielna przez żadne z tych liczb.''')
podzielnaprzez3lub5lub7()


# 9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7

def podzielnaprzez3i5i7(liczba_4 = input('''Sprawdź czy dana liczba jest podzielna przez 3 i 5 i 7.
Podaj liczbę: ''')):
    dz1 = 3
    dz2 = 5
    dz3 = 7
    liczba_4 = int(liczba_4)
    if liczba_4 % 3 == 0 and liczba_4 % 5 == 0 and liczba_4 % 7 == 0:
        print("Liczba jest podzielna przez 3 i 5 i 7.")
    else:
        print("Liczba nie jest podzielna przez 3 i 5 i 7.")
podzielnaprzez3i5i7()


# 10. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym

def rokprzestepny(rok = input('''Sprawdź czy podany rok jest rokiem przestępnym.
Podaj datę: ''')):
    rok = int(rok)
    if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
        print("Podany rok jest rokiem przestępnym.")
    else:
        print("Podany rok nie jest rokiem przestępnym.")
rokprzestepny()


#11) Program rysujący piramidę o określonej wysokości, np dla 3
  #
 ###
#####

def piramida(n = input('''Narysuj piramidę o określonej wysokości.
Wprowadź wysokość prostokąta: ''')):
    n = int(n)
    print('\n'.join((' ' * (n - i) + '*' * (i * 2 + 1) for i in range(n))))
piramida()





