from moduly.calculators import calculatorCtoF
from moduly.calculators import calculatorFtoC
from moduly.calculators import pole_kola
from moduly.binarne import binarytodecimal
from moduly.calculators import rokprzestepny
from moduly.drawnings import rectangle
from moduly.drawnings import piramida
from moduly.numbers import pierwsza_ostatnia_cyfra
from moduly.numbers import podzielnaprzez3lub5lub7
from moduly.numbers import podzielnaprzez3i5i7
from moduly.calculators import wiekpsa
from moduly.numbers import parzysta
import random


def multitool():
    print('Witaj w Multitool Python Program!'
              '\n Wybierz program, który Cię interesuje'
              '\n - 1) Kalkulator stopni Celcjusza na Fahrenheita'
              '\n - 2) Kalkulator stopni Fahrenheita na Celcjusza'
              '\n - 3) Obliczanie pola powierzchni koła o zadanym promieniu'
              '\n - 4) Przeliczanie liczby zapisanej w formacie binarnym na system dziesiętny (w trakcie tworzenia)'
              '\n - 5) Program do sprawdzania czy podany rok jest rokiem przestępnym'
              '\n - 6) Program, który rysuje prostokąt o zadanych rozmiarach'
              '\n - 7) Program rysujący piramidę o określonej wysokości'
              '\n - 8) Program, który podaje pierwszą i ostatnią cyfrę podanej liczby'
              '\n - 9) Program do rozpoznawania czy podana liczba jest parzysta czy nie'
              '\n - 10) Program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7'
              '\n - 11) Program do sprawdzania czy liczba jest podzielna przez 3 i 5 i 7'
              '\n - 12) Program do obliczania wieku psa'
              '\n - 13) Wybierz program losowo'
              '\n - 0) Wyjście z programu')
    program = int(input("Co chcesz zrobić? Twój wybór: "))
    funkcje = ['', calculatorCtoF, calculatorFtoC, pole_kola, binarytodecimal,
               rokprzestepny, rectangle, piramida, pierwsza_ostatnia_cyfra, parzysta,
               podzielnaprzez3lub5lub7, podzielnaprzez3i5i7, wiekpsa]
    if program == 1:
        funkcje[program]()
    elif program == 2:
        funkcje[program]()
    elif program == 3:
        funkcje[program]()
    elif program == 4:
        funkcje[program]()
    elif program == 5:
        funkcje[program]()
    elif program == 6:
        funkcje[program]()
    elif program == 7:
        funkcje[program]()
    elif program == 8:
        funkcje[program]()
    elif program == 9:
        funkcje[program]()
    elif program == 10:
        funkcje[program]()
    elif program == 11:
        funkcje[program]()
    elif program == 12:
        funkcje[program]()
    elif program == 13:
        random.choice(funkcje)()
    elif program == 0:
        print("Mam nadzieję, że jeszcze wrócisz! Do zobaczenia :)")
multitool()
