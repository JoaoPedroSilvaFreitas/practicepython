__author__ = 'joao'

numero = int(input("NÚMERO:"))
if numero % 2 == 0:
    if numero % 4 == 0:
        print(str(numero) + " é multiplo de 4")
    else:
        print(str(numero) + " é par")
else:
    print(str(numero) + " é ímpar")

numero2 = int(input("NÚMERO:"))
if numero % numero2 == 0:
    print(str(numero) + " é multiplo de " + str(numero2))
else:
    print(str(numero) + " não é multiplo de " + str(numero2))