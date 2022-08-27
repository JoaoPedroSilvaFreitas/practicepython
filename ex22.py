__author__ = 'joao'

    

def readRandomLetters(word):
    with open('www.practicepython.org/output/randomLetters.txt', 'r') as open_file:
        all_text = open_file.read()
        print("found" if all_text.count(word) > 0 else "did not find")
        
def readRandomNames(name):
    with open('www.practicepython.org/output/randomNames.txt', 'r') as open_file:
        all_text = open_file.read()
        print("found" if all_text.count(name) > 0 else "did not find")

def readRandomNumbers(number):
    with open('www.practicepython.org/output/randomNumbers.txt', 'r') as open_file:
        all_text = open_file.read()
        print("found" if all_text.count(str(number)) > 0 else "did not find")

def printMenu():
    print("--------------Menu--------------")
    print("1 - read random letters")
    print("2 - read random names")
    print("3 - read random numbers")
    print("0 - exit")
    option = input("select: ")
    return option

while True:
    option = printMenu()
    if option == '1': readRandomLetters(input("search word: "))
    elif option == '2': readRandomNames(input("search name: "))
    elif option == '3': readRandomNumbers(int(input("search number: ")))
    elif option == '0' : break
    else : print("Invalid option!")
