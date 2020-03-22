
### 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)
# wzór °F = (°C × 1.8) + 32

def calculatorCtoF(x=1.8,y=32):
    print("Kalkulator °C do °F.")
    temperatura_C = None
    while temperatura_C is None:
        try:
            temperatura_C = float(input("Podaj temperaturę w °C: "))
            wynik = (temperatura_C * x) + y
            print(f'Obliczenia: ({temperatura_C} * {x}) + {y}.')
            print(f'Wynik to: {wynik}°F. Dziękujemy za skorzyskanie z kalkulatora.')
            break
        except:
            print("Spróbuj ponownie.")


## 2. Program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
# wzór = (°F − 32)/1.8

def calculatorFtoC(x=1.8,y=32):
    print("Kalkulator °F do °C.")
    temperatura_F = None
    while temperatura_F is None:
        try:
            temperatura_F = float(input("Podaj temperaturę w °F: "))
            wynik = ((temperatura_F - y) / x)
            print(f'Obliczenia: ({temperatura_F} - {y}) / {x}.')
            print(f'Wynik to: {wynik}°C. Dziękujemy za skorzystanie z kalkulatora.')
            break
        except:
            print("Spróbuj ponownie.")


## 3. Program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
# wzór  π r²

def pole_kola(π=3.14,):
    print("Kalkulator powierzchni koła.")
    r = None
    while r is None:
        try:
            r = float(input("Podaj promień [w cm]: "))
            pole = π * r ** 2
            print(f'Obliczenia: {π} * {r} ^ 2.')
            print(f'Wynik to: {pole}cm. Dziękujemy za skorzystanie z kalkulatora.')
            break
        except:
            print("Podano złą wartość. Spróbuj ponownie.")


## Program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny
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



## Program do sprawdzania czy podany rok jest rokiem przestępnym
def rokprzestepny():
    rok = None
    while rok is None:
        try:
            import calendar
            print("Sprawdź czy podany rok jest przestępny.")
            rok = int(input("Podaj datę: "))
            calendar.isleap(rok)
            if calendar.isleap(rok) is True:
                print("To jest rok przestępny.")
            else:
                print("To nie jest rok przestępny.")
        except:
            print("Podana wartość jest nieprawidłowa. Spróbuj ponownie.")
