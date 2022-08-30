__author__ = 'joao'

from random import randint, seed

def pickWord():
    lines = []
    file = open("input/words.txt", 'r')
    while True:
        line = file.readline()
        lines.append(line)
        if not line:
            break
    file.close()
    return lines[randint(0,len(lines))]

def guessLetter(word, lettersGuessed, letters):
    
    letter = input("Letter: ").upper()
    while letters.count(letter) != 0:
        letter = input("Letter: ").upper()

    letters.append(letter)

    if word.count(letter) == 0: 
        print("Wrong!")
        return False

    for i in range(0,len(word)):
        if word[i] == letter: 
            lettersGuessed[i] = True
    return True

def printWord(word, lettersGuessed):
    for i in range(0,len(word)):
        if lettersGuessed[i] == True: print(word[i] + " ", end = '')
        else: print("_ ", end = '')
    print()

def startGame():
    wrong = 6
    lettersGuessed = []
    letters = []
    word = pickWord().rstrip()

    for i in range(0, len(word)):
        lettersGuessed.append(False)

    while True:
        print("_____________________________________________")
        print(str(wrong) + " guesses left")
        printWord(word, lettersGuessed)
        if not guessLetter(word, lettersGuessed, letters): wrong -= 1

        if wrong == 0:
            print("You lost! the word was: " + word)
            return
        
        if lettersGuessed.count(False) == 0:
            print("You won! the word was: " + word)
            return


def printMenu():
    print("--------------Hangman--------------")
    print("1 - Play")
    print("0 - Exit")
    option = input("Select: ")
    return option

while True:
    option = printMenu()
    if option == '1': startGame() 
    elif option == '0': break
    else : print("Invalid option!")
