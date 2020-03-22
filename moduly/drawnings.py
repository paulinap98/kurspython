## Program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
#     | (bok)
#     - (góra/dół)
#     + (wierzchołek)
def rectangle():
    print("Narysuj prostokąt o określonym rozmiarze.")
    a = True
    b = True
    while a and b is True:
        try:
            a = int(input("Podaj wysokość prostokąta: "))
            b = int(input("Podaj szerokość prostokąta: "))
            puste = ' ' * b
            sciana = '|'
            wysokosc = f'{sciana}{puste}{sciana}'
            szerokosc = "-" * b
            print("Tak wygląda twój prostokąt: ")
            print(f'+{szerokosc}+')
            for sciana in range(a):
                print(wysokosc)
            print(f'+{szerokosc}+')
        except:
            print("Podane wartości są nieprawidłowe. Spróbuj ponownie.")




## Program rysujący piramidę o określonej wysokości
def piramida():
    print("Narysuj piramidę o określonej wielkości.")
    n = int(input("Podaj wysokość piramidy: "))
    for i in range (n):
        print((' ' * (n - i) + '#' * (i * 2 + 1)))
