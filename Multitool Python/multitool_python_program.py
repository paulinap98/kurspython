
print('Witaj w Multitool Python Program!')
wybor = None
while wybor is None:
    try:
        print(
        '''Wybierz numer programu, który Cię interesuje:
            1) Kalkulator stopni Celsjusza na Fahrenheita
            2) Kalkulator stopni Fahrenheita na Celsjusza
            3) Obliczenie pola powierzchni koła o zadanym promieniu
            4) Przeliczanie liczby zapisanej w formacie binarnym na system dziesiętny (w budowie ;))
            5) Program do sprawdzania czy podany rok jest rokiem przestępnym
            6) Program, który rysuje prostokąt o zadanych rozmiarach
            7) Program rysujący piramidę o określonej wysokości
            8) Program, który podaje pierwszą i ostatnią cyfrę podanej liczby
            9) Program do rozpoznawania czy podana liczba jest parzysta czy nie
            10) Program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7
            11) Program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7
            R) Wybierz program losowo
            X) Wyjście z programu''')
        wybor = int(input("Twój wybór: "))
        if wybor == 1:
            from moduly.calculators import calculatorCtoF
            calculatorCtoF()
        elif wybor == 2:
            from moduly.calculators import calculatorFtoC
            calculatorFtoC()
        elif wybor == 3:
            from moduly.calculators import pole_kola
            pole_kola()
        elif wybor == 4:
            from moduly.binarne import binarytodecimal
            binarytodecimal()
        elif wybor == 5:
            from moduly.calculators import rokprzestepny
        elif wybor == 6:
            from moduly.drawnings import rectangle
            rectangle()
        elif wybor == 7:
            from moduly.drawnings import piramida
            piramida()
        elif wybor == 8:
            from moduly.numbers import pierwsza_ostatnia_cyfra
            pierwsza_ostatnia_cyfra()
        elif wybor == 9:
            from moduly.numbers import parzysta
            parzysta()
        elif wybor == 10:
            from moduly.numbers import podzielnaprzez3lub5lub7
            podzielnaprzez3lub5lub7()
        elif wybor == 11:
            from moduly.numbers import podzielnaprzez3i5i7
            podzielnaprzez3i5i7()
        elif wybor == 12:
            from moduly.calculators import wiekpsa
            wiekpsa()
        elif wybor == 13:
            print("Mam nadzieję, że jeszcze wrócisz! Miłego dnia :)")
            break
    except:
        print("Wpisane dane są nieprawidłowe. Spróbuj jeszcze raz.")

