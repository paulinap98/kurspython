# pobieranie danych od użytkownika

imię = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")

treść = f'Witaj {imię.capitalize()} {nazwisko.capitalize()}. Dziękujemy za odwiedziny!'
print(treść)

print('''

''')

liczba_1 = 123
liczba_2 = 4.5
liczba_3 = int("1") #int zamienia stringa (w tym przypadku) na int
print(liczba_1 * liczba_2)
print(liczba_1 / liczba_3)


zmienna_1 = "Ala"
zmienna_2 = " ma kota"
print(zmienna_1 + zmienna_2)


#whitespaces \n \t
sciezka_do_pliku = "c:\\documents\nowy_folder"
print(sciezka_do_pliku)
#\n od nowej linijki

sciezka_do_pliku1 = "c\\documents\tatry"
print(sciezka_do_pliku1)
#\t

sciezka_do_pliku2 = "c:\\documents\\nowy folder\\tatry"
print(sciezka_do_pliku2)
#\\ usuwa "aktywność" \

sciezka_do_pliku3 = "c:\\\documents\\nowy folder\\tatry"
print(sciezka_do_pliku3)
# 3 razy \\\ zeby dwa razy sie pokazalo \ po c:

sciezka_do_pliku4 = r"c:\\documents\nowy folder\tatry"
print(sciezka_do_pliku4)
#r przed zawartością nie potraktuje tego inaczej


print(imię + '\n' + nazwisko)
print(imię + '\n\n\n' + nazwisko)
print(imię + 2 * '\n' + nazwisko)
print(imię.capitalize() + '\n' + nazwisko)

zmienna3 = 1
typ = type(zmienna3)
print(typ)
#sprawdza jaki to typ 1=int

zmienna4 = "1"
typ = type(zmienna4)
print(typ)

zmienna5 = 1.5
typ = type(zmienna5)
print(typ)


zmienna7 = True
typ = type(zmienna7)
print(typ)

zmienna10 = input("Wpisz coś: ")
typ = type(zmienna10)
print(typ)
#!!! przy input zawsze wyjdzie str



wartosc_1 = input("Podaj jedną liczbe: ")
wartosc_2 = input("Podaj drugą liczbe: ")
print(wartosc_1 + wartosc_2)
#tutaj nie zmienilismy na int, tylko polaczylismy cyfry


liczba_pierwsza = int(wartosc_1)
liczba_druga = int(wartosc_2)
print(liczba_pierwsza + liczba_druga)
#tutaj wyjdzie prawidlowy wynik


#inaczej można w jednej linijce
print(int(input("Podaj liczbę: ")) + int(input("Podaj liczbę: ")))

#jeśli nie mamy liczby całkowitej tylko ułamek, to bierzemy float


#int() zmienia parametr na int
#str() zmienia parametr na string


zdanie = "Ala ma kota."

print(zdanie[7])
print(zdanie[7:9])

print(zdanie[1:8])

print(zdanie[1:8:2])
#co dwa wyswietla

uciete_zdanie = zdanie[1:8:5]
print(len(zdanie[1:8:5]))

print(len(zdanie))

print(zdanie[-1])

dlugosc = len(zdanie)
print(zdanie[dlugosc-1])

#przedział lewy jest zamknięty, prawy otwarty, a trzeci to przeskok

ostatni_znak = zdanie[-1]

if ostatni_znak == '!':
    print('Nie krzycz na mnie')
else:
    print('Dziękuję.')


