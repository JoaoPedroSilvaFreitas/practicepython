__author__ = 'joao'

from random import randint, seed
import random
import string


def weakPassword(): ##only lower case letters max size = 8
    with open('output/randomPassword.txt', 'a') as open_file:
        ##password = []
        password = ""
        for i in range(0,randint(5,8)):
            ##password.append(random.choice(string.ascii_lowercase))
            password += random.choice(string.ascii_lowercase)
        ##print(*password)
        open_file.write(password)
        open_file.write("\n")
            

def regularPassword(): ## numbers letters max size = 12
    with open('output/randomPassword.txt', 'a') as open_file:
        ##password = []
        password = ""
        for i in range(0,randint(8,12)):
            if random.choice([True, False]):
                ##password.append(random.choice(string.ascii_letters))
                password += random.choice(string.ascii_letters)
            else : password += str(randint(0,9)) ##password.append(randint(0,9))
        ##print(*password)
        open_file.write(password)
        open_file.write("\n")
        

def strongPassword(): ## numbers letters special chars in random order max size = 20
    with open('output/randomPassword.txt', 'a') as open_file:
        ##password = []
        password = ""
        specialChars = '@#$%&+=;:><.,!-_{[}]()*çãõáàóòéèúùíì'
        for i in range(0,randint(8,12)):
            type = random.choice([1,2,3])
            if type == 1:
                ##password.append(random.choice(string.ascii_letters))
                password += random.choice(string.ascii_letters)
            elif type == 2:
                ##password.append(randint(0,9))
                password += str(randint(0,9))
            elif type == 3:
                ##password.append(random.choice(specialChars))
                password += random.choice(specialChars)
        open_file.write(password)
        open_file.write("\n")
        ##print(*password)

def printMenu():
    print("--------------Menu--------------")
    print("1 - weak password")
    print("2 - regular password")
    print("3 - strong password")
    print("0 - exit")
    option = input("select: ")
    return option

while True:
    option = printMenu()
    if option == '1': weakPassword()
    elif option == '2': regularPassword()
    elif option == '3': strongPassword()
    elif option == '0' : break
    else : print("Invalid option!")