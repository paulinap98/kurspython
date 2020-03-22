## Program, który podaje pierwszą i ostatnią cyfrę podanej liczby
def pierwsza_ostatnia_cyfra():
    print("Pierwsza i ostatnia cyfra danej liczby.")
    value = None
    while value is None:
        try:
            value = int(input("Podaj dowolną liczbę: "))
            value = str(value)
            first = value[0]
            last = value[-1]
            print(f'Pierwsza cyfra to {first}, a ostatnia cyfra to {last}.')
            break
        except:
            print("Podane wartości są nieprawidłowe. Spróbuj ponownie.")


## Program do rozpoznawania czy podana liczba jest parzysta czy nie.
def parzysta():
    print("Sprawdź czy dana liczba jest parzysta.")
    liczba = True
    while liczba is True:
        try:
            liczba = int(input("Podaj liczbę: "))
            if liczba % 2 == 0:
                print("Liczba jest parzysta.")
            else:
                print("Liczba jest nieparzysta.")
        except:
            print("Podano nieprawidłowe dane. Spróbuj ponownie.")

## Program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7
def podzielnaprzez3lub5lub7(dz1=3, dz2=5, dz3=7):
    liczba = True
    while liczba is True:
        try:
            liczba = int(input("Podaj dowolną liczbę: "))
            if liczba % dz1 == 0 and liczba % dz2 == 0 and liczba % dz3 == 0:
                print(f'''Liczba jest podzielna przez {dz1}, {dz2} i {dz3}.''')
            elif liczba % dz1 == 0 and liczba % dz2 == 0 and liczba % dz3 != 0:
                print(f'''Liczba jest podzielna przez {dz1} i {dz2}.''')
            elif liczba % dz2 == 0 and liczba % dz3 == 0 and liczba % dz1 != 0:
                print(f'''Liczba jest podzielna przez {dz2} i {dz3}.''')
            elif liczba % dz1 == 0 and liczba % dz3 == 0 and liczba % dz2 != 0:
                print(f'''Liczba jest podzielna przez {dz1} i {dz3}.''')
            elif liczba % dz1 == 0:
                print(f'''Liczba jest podzielna tylko przez {dz1}.''')
            elif liczba % dz2 == 0:
                print(f'''Liczba jest podzielna tylko przez {dz2}.''')
            elif liczba % dz3 == 0:
                print(f'''Liczba jest podzielna tylko przez {dz3}.''')
            else:
                print(f'''Liczba nie jest podzielna przez żadne z tych liczb.''')
        except:
            print("Podano niewłaściwe wartości. Spróbuj ponownie.")


## Program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7
def podzielnaprzez3i5i7(d3=3, d5=5, d7=7):
    print("Sprawdź czy dana liczba jest podzielna przez 3 i 5 i 7.")
    liczba = True
    while liczba is True:
        try:
            liczba = int(input("Podaj dowolną liczbę: "))
            if liczba % 3 == 0 and liczba % 5 == 0 and liczba % 7 == 0:
                print(f'Liczba jest podzielna przez {d3}, {d5} i {d7}.')
            else:
                print(f'Liczba nie jest podzielna przez {d3}, {d5} i {d7}.')
                break
        except:
            print("Podane dane są nieprawidłowe. Spróbuj ponownie.")


##