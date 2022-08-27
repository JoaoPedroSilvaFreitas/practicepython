__author__ = 'joao'

from random import randint, seed

def createList():
    number = randint(0,100)
    list = []
    for i in range(0,randint(1,10)):
        list.append(number + i)
    return list


list = createList()
number = int(input("number: "))

print("list has " + str(number) if list.count(number) > 0 else "list does not have " + str(number))

print(*list)