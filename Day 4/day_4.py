lista = [1, 2, 3]
nowa_lista = lista
print(lista)
lista[0] = 'jeden'
print(nowa_lista)

lista = ['A', 'B', 'C']
prawdziwa_kopia = lista.copy()
print(lista)
print(prawdziwa_kopia)
print(lista)

lista = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
import copy
nowa_lista = copy.deepcopy(lista)
print(lista[1][1])
lista[1][1] = 'X'
print(nowa_lista[1][1])
print(lista[1][1])

