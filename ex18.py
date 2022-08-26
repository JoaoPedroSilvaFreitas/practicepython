__author__ = 'joao'

from random import randint, seed

def initGame():
    attempts = 1
    number = randint(1000,9999)
    print("Guess the number or type 0 to quit")
    while True:
        cows = 0
        bulls = 0
        guess = input("Number: ")

        if guess == "0" : break
        elif guess == str(number) : 
            print("Congratulations!! you guessed the number " + str(number) + " with " + str(attempts) + " attempts!") 
            break

        for i in range(0,3):
            if guess[i] == str(number)[i] : cows += 1
            elif str(number).count(guess[i]) >= 1 and guess[i] != str(number)[i]: bulls += 1
        attempts += 1
        print(str(cows) + " cows, " + str(bulls) + " bulls")


def printMenu():
    print("-----------Cows and Bulls-----------")
    print("1 - Play")
    print("0 - Exit")
    return input("Select: ")

while True:
    option = printMenu()
    if option == '1': initGame()
    elif option == '0': break
    else : print("Invalid option!")
