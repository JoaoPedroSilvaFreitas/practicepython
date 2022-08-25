__author__ = 'joao'

from random import randint, seed

number = randint(1,9)
exit = False
guessed = 0

while exit == False:
    guess = input("")
    
    if guess == "exit":
        print("Numbers guessed: " + str(guessed))
        break

    if int(guess) > number : print("to high")
    elif int(guess) < number : print("to low")
    else: 
        print("Congratulations! you guessed the number")
        guessed += 1
        number = randint(1,9)


