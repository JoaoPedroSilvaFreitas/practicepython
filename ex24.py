__author__ = 'joao'

def printBlock(size):
    for i in range(0, size):
        for j in range(0, size): 
            print(" --- ", end = '')
        print()
        for k in range(0, size): 
            print("|   |", end = '')
        if i == size - 1: 
            print()
            for n in range(0, size): print(" --- ", end = '')
        print()

printBlock(int(input("size: ")))