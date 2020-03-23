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