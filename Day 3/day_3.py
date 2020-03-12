# tytul = "Książka pt: \"Kot w butach\"."
# print(tytul)
#
# tytul1 = 'Książka pt: "Kot w butach".'
# print(tytul1)
#
# tytul2 = "I'm"
# print(tytul2)
#
# tytul3 = 'I\'m'
# print(tytul3)
#
# liczba = 1
# liczba2 = 2
# print('Wprowadziłeś liczbę: ' + str(liczba))
# print(f'Wprowadziłeś liczbę: {liczba}')
# print('Wprowadziłeś liczbę: {} {a} {a}'.format(liczba, a=liczba2))
#
# zestaw_liczb = range(0,100000)
# print(zestaw_liczb)
#
# lista = [1,2,3,4,5,6,7,8,9,10]
# print(lista)
# lista_2 = list('dwa')
# print(lista_2)
# lista_3 = ['dwa']
# print(lista_3)
#
# lista_4 = list(range(0, 100))
# print(lista_4)
#
#
# lista_5 = ['zero', 1, 'trzeci', 'dom']
# print(lista_5)
# print(lista_5[0])
# print(lista_5[3])
# print(lista_5[-1])
# print(lista_5[::-1])
# lista_5[1] = 'jeden'
# print(lista_5)
#
# print(zestaw_liczb[0] == 23)
# print(zestaw_liczb[23] == 23)
# lista_5.append('nowy element')
# print(lista_5)
# del(lista_5[0]) #usuwa pierwszy element z listy i przy okazji przesuwa indeksy
# print(lista_5)
# lista_5.remove('dom')
# print(lista_5) #usuwa określony element z listy
#
#
# if 'dom123' in lista_5:
#     lista_5.remove('dom123')
# else:
#     print('Taki element nie istnieje.')
#
# print(lista_5)
#
# if 'trzeci' in lista_5:
#     lista_5.remove('trzeci')
# else:
#     print("Taki element nie istnieje.")
#
# print(lista_5)

# krotka = ("jeden", "dwa", "trzy")
# print(krotka)
# print(type(krotka))
# print(len(krotka))
# print(krotka[0])
# #krotki nie można modyfikować, ale można ją usunąć del(krotka)



# while True:
#     #nieskończona pętla
#     pass

# while True:
#     #nieskończona pętla
#     print('.')

# czy_kontynuować = 'T'

# while czy_kontynuować == 'T':
#     #nieskończona pętla
#     print('.')

# while czy_kontynuować == 'T':
#     print('.')
#     czy_kontynuować = input('Czy kontynuować [T/N]? ')
#
# print('Koniec')

licznik = 0

# while licznik <= 10: #wykona się tak długo, aż licznik będzie większy niż 10
#     #print(licznik)
#     if licznik == 5:
#         continue
#     else:
#         print(licznik)
#     licznik += 1  #skrócony zapis tego na dole
#     #licznik = licznik + 1
#
# print('Koniec')


# while licznik < 10:
#     licznik += 1
#     if licznik in [5,8]:
#         continue
#     print(licznik)
# print('Koniec')

# while licznik < 10:
#     licznik += 1
#     if licznik == 5 or licznik == 8:
#         continue
#     print(licznik)
# print('Koniec')

# while licznik < 10:
#     licznik += 1
#     if licznik in [5,8]:
#         break
#     print(licznik)
# print('Koniec')


zdanie = 'Ala!'

#for litera in zdanie:
   # print(litera)
#bierze i drukuje po kolei elementy

# print(litera) #tutaj wcześniej nie jest zdefiniowana, bo w forze bierze tutaj ostatnią literę.


# for litera in zdanie:
#     if litera in ['a', 'A']:
#         continue
#     print(litera)

lista = ['jeden', 'dwa', 'dom']
calkowity_rozmiar = 0

for element in lista:
    rozmiar_elementu = len(element)
    calkowity_rozmiar += rozmiar_elementu   #+= lepiej używać
print(calkowity_rozmiar)
print('Koniec')

for i in range(10):
    print(i)


for j in range(0,100,3): #podzielne przez 3
    print(j)

