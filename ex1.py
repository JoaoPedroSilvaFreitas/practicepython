__author__ = 'joao'

nome = input("NOME:")
idade = int(input("IDADE:"))
ano = 100 - idade + 2022
print(nome + " em " + str(ano) + " você terá 100 anos")

repetir = int(input("REPETIR:"))

i = 0
while i < repetir:
        print(nome + " em " + str(ano) + " você terá 100 anos\n")
        i += 1
