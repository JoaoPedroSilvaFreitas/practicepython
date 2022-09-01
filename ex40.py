__author__ = 'joao'


from random import randint, seed

def startGame():
    number = randint(1,9)
    guessed = 0

    
    while True:
        guess = int(input("Type a number between 0-9 (0 to quit): "))
        while guess > 9 or guess < 0: guess = int(input(""))
        
        if guess == 0:
            print(f"Numbers guessed: {guessed}")
            break

        if guess > number : print("to high")
        elif guess < number : print("to low")
        else: 
            print("Congratulations! you guessed the number")
            guessed += 1
            number = randint(1,9)

def printMenu():
    print("--------------Guessing Game 1--------------")
    print("1 - Play")
    print("0 - Exit")
    return input("Select: ")

while True:
    option = printMenu()
    if option == '1': startGame()
    elif option == '0': break
    else : print("Invalid option!")

