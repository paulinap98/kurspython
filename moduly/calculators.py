
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

## Kalkulator do wyliczania wieku psa.
#     Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata
# Np: 15 ludzkich lat to 73 psie lata

def wiekpsa():
    print("Kalkulator do wyliczania wieku psa.")
    wiek = None
    while wiek is None:
        try:
            wiek = float(input("Podaj wiek psa: "))
            mniejniz2 = wiek * 10.5
            wiecejniz2 = (wiek - 2)  * 4 + 21
            if wiek <= 2:
                print(f'W ludzkich latach twój pies ma: {mniejniz2} lata.')
            elif wiek > 2:
                print(f'W ludzkich latach twój pies ma: {wiecejniz2} lat.')
                break
        except:
            print("Podana wartość jest nieprawidłowa. Spróbuj ponownie.")

