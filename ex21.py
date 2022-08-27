__author__ = 'joao'

from cmath import inf
from random import randint, seed
import random
import string

#outro jeito de abrir arquivo
#open_file = open('file_to_save.txt', 'w')
#open_file.write('A string to write')
#open_file.close()

def writeRandomNumbers(quantity):
    with open('output/randomNumbers.txt', 'w') as open_file:
        for i in range(0,quantity):
            for j in range(1,randint(1,20)):
                open_file.write(random.choice(string.digits))
            open_file.write("\n")

def writeRandomNames(quantity):
    names = ("Anderson", "Alvaro", "Augusto", "Adrian", "André", "Ariel", "Antônio", "Bruno", "Benício", "Caique"
    , "Caio", "Cauã", "Daniel", "Davi", "Denis", "Eduardo", "Enzo", "Fabricio", "Fernando", "Giovane"
    , "Gabriel", "Gustavo", "Heitor", "Hudson", "Henrique", "Hugo", "Igor", "Italo", "Ivan", "Jaime", "João",  "José"
    , "Júlio", "Juliano", "Kauã", "Kildare", "Luan", "Leonardo", "Miguel", "Marcos", "Marcio", "Mateus", "Natan", "Otávio"
    , "Paulo", "Pedro", "Renato", "Roberto", "Rafael", "Samuel", "Thiago", "Tiago", "Victor"
    , "Amanda", "Amélia", "Ana", "Bruna", "Bianca", "Camila", "Carolina", "Caroline", "Carol", "Cecília", "Dhayana", "Daniela", "Diana"
    , "Daiana", "Denise", "Eduarda", "Elisa", "Emili", "Eva", "Fernanda", "Ivone", "Isadora", "Joana", "Janaina", "Jaqueline"
    , "Karoline", "Laura", "Lívia", "Letícia", "Maria", "Manuela", "Marina", "Mariana", "Marcela" , "Noemi" 
    , "Noemia", "Nicole", "Nubia" , "Olivia" , "Paula", "Poliana", "Renata", "Rafaela", "Roberla", "Rubia", "Regina"
    , "Sofia", "Sônia", "Sabrina", "Tatiana", "Tamires", "Tuane", "Vanessa", "Vitória")

    with open('output/randomNames.txt', 'w') as open_file:
        for i in range(0,quantity):
            open_file.write(random.choice(names))
            open_file.write("\n")

def writeRandomLetters(quantity):
    with open('output/randomLetters.txt', 'w') as open_file:
        for i in range(0,quantity):
            for j in range(0,randint(0,20)):
                open_file.write(random.choice(string.ascii_lowercase))
            open_file.write("\n" if random.choice([True,False,False,False,False]) else " ")

def printMenu():
    print("--------------Menu--------------")
    print("1 - write random letters")
    print("2 - write random names")
    print("3 - write random numbers")
    print("0 - exit")
    option = input("select: ")
    return option

while True:
    option = printMenu()
    if option == '1': writeRandomLetters(int(input("how many words: ")))
    elif option == '2': writeRandomNames(int(input("how many names: ")))
    elif option == '3': writeRandomNumbers(int(input("how many numbers: ")))
    elif option == '0' : break
    else : print("Invalid option!")
