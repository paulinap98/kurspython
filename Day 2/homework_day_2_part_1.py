
# 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)
# wzór °F = (°C × 1.8) + 32

print('Kalkulator temperatury °C do °F.')
temperatura = input('Podaj temperaturę w °C: ')
temperatura = int(temperatura)

wartość_1 = 1.8
wartość_2 = 32

wzór = (temperatura * wartość_1) + wartość_2
print(f'Obliczenia: {temperatura}°C x 1.8 + 32')
print(f'''Wynik: {wzór}°F. 
Dziękujemy za skorzystanie z kalkulatora.''')


# 2. Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
# wzór = (°F − 32)/1.8

print('Kalkulator temperatury °F do °C.')
temperatura_1 = input('Podaj temperaturę w °F: ')
temperatura_1 = int(temperatura_1)

wzór_1 = (temperatura_1 - wartość_2) / wartość_1
print(f'Obliczenia: {temperatura_1}°F - 32 / 1.8')
print(f'''Wynik: {wzór_1}°C. 
Dziękujemy za skorzystanie z kalkulatora.''')


# 3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
# wzór  π r²


print('Kalkulator pola powierzchni koła o zadanym promieniu.')
promień = input('Podaj promień koła [w cm]: ')
promień = int(promień)
π = 3.14
pole = π * promień ** 2
print(f'Obliczenia: π * {promień}cm²')
print(f'''Wynik: {pole}cm. 
Dziękujemy za skorzystanie z kalkulatora.''')

# 4. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby

print('Pierwsza i ostatnia cyfra danej liczby.')
liczba = input('Podaj dowolną liczbę: ')
liczba = str(liczba)

pierwsza_cyfra = liczba[0]
ostatnia_cyfra = liczba[-1]
print(f'''Pierwsza cyfra to {liczba[0]}.''')
print(f'''Ostatnia cyfra to {liczba[-1]}.''')

