__author__ = 'joao'

from random import randint, seed

def guessNumber(min, max):
    number = randint(min, max)
    print(str(number))
    return number

def printInGameMenu():
    print("1 - To low!")
    print("2 - To high!")
    print("3 - Found!")
    print("0 - Exit")
    option = input("Select: ")
    return option

def guessingGameComputer():
    count = 0
    min = 0
    max = 100

    number = guessNumber(min, max)

    while True: 
        count += 1
        option = printInGameMenu()

        if option == '1': 
            if min < number: min = number
            number = guessNumber(min + 1,max)

        elif option == '2': 
            if max > number: max = number
            number = guessNumber(min,max - 1)

        elif option == '3': 
            print("The computer guessed the number " + str(number) +  " in " + str(count) + " attempts") 
            break

        elif option == '0': break

        else : print("Invalid option!")

def printMenu():
    print("--------------Guessing Game 2--------------")
    print("1 - Play")
    print("0 - Exit")
    option = input("Select: ")
    return option

while True:
    option = printMenu()
    if option == '1': guessingGameComputer() 
    elif option == '0': break
    else : print("Invalid option!")