__author__ = 'joao'

lista = [10]

for i in range(0,10):
    print(str(i) + ":", end='')
    n = int(input())
    lista.append(n)

lista.sort() ##essa função aqui ordena a lista com com um algoritmo de ordenação chamado TimSort

for i in range(0,10):
    if lista[i] < 5:
        print(str(lista[i]) + "  ", end='')
print()
    
n = int(input())

for i in range(0,10):
    if lista[i] < n:
        print(str(lista[i]) + "  ", end='')
print()



##Resposta do site pq achei interessante aquele print no final
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# basic problem:
for x in a:
    if x< 5: print(x)
# combine challenges 1 and 2:
print( [ x for x in a if x<5 ] )