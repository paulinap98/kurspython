# lista = [1, 2, 3]
# nowa_lista = lista
# print(lista)
# lista[0] = 'jeden'
# print(nowa_lista)
#
# lista = ['A', 'B', 'C']
# prawdziwa_kopia = lista.copy()
# print(lista)
# print(prawdziwa_kopia)
# print(lista)
#
# lista = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# import copy
# nowa_lista = copy.deepcopy(lista)
# print(lista[1][1])
# lista[1][1] = 'X'
# print(nowa_lista[1][1])
# print(lista[1][1])
#

# def hej(imie, nazwisko):
#     print(f'Dzień dobry, {imie} {nazwisko}')
#     #print('Dzień dobry ' + str(imie))
#     #print('Dzień dobry {}'.format(imie))
#
# # hej()
# # # dzien_dobry = hej  #bez ()
# # # dzien_dobry()
# # # print(dzien_dobry)
#
# hej('Paulina', 'P')

def hej(imie, nazwisko="P"):
    print(f'Dzień dobry, {imie} {nazwisko}')

hej('Paulina')
hej(imie='Ewa', nazwisko='Gggg')
hej(nazwisko='Paulina', imie='Kowalska')

#
# def test(x,y):
#     pass
#
# test(y=2, x=3)

imie = input('Podaj imie: ')
hej(imie)
hej(input('Podaj imię: '))
print(imie)

def dodaj(x,y):
    suma = x + y
    return suma
x = input('Podaj wartość: ')
y = input('Podaj drugą wartość: ')
x = float(x)
y = float(y)
wynik = dodaj(x,y)
print(wynik)

# def dodaj(x, y):
#     suma = float(x) + float(y)
#     return suma
#
# wynik = dodaj (x, y)
# print(wynik)

# def dodaj(x, y):
#     suma = float(x) + float(y)
#     return dodaj(x, y)                        to jest funkcja rekurencyjna
#
# wynik = dodaj("2.1", "7")
# print(wynik)


