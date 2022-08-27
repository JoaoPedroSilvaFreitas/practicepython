__author__ = 'joao'

def writePrimeNumbersToFile():
    number = int(input("Prime: "))
    with open('output/primeNumbers.txt', 'w') as open_file:
        for i in range(1,number + 1):
            if i % 2 != 0:
                open_file.write(str(i) + "\n")


def writeHappyNumbersToFile():
    number = int(input("Happy: "))
    with open('output/happyNumbers.txt', 'w') as open_file:
        for i in range(1,number + 1):
            if i % 2 != 0:
                open_file.write(str(i) + "\n")

def fileOverlap():
    file1 = open('output/primeNumbers.txt', 'r')
    file2 = open('output/happyNumbers.txt', 'r')
    while True:

        line1 = file1.readline()
        line2 = file2.readline()

        if line1 == line2:
            print(line1, end='')

        if not line1 or not line2:
            break
    
    file1.close()
    file2.close()

def printMenu():
    print("--------------Menu--------------")
    print("1 - write prime numbers")
    print("2 - write happy numbers")
    print("3 - file overlap")
    print("0 - exit")
    option = input("select: ")
    return option

while True:
    option = printMenu()
    if option == '1': writePrimeNumbersToFile()
    elif option == '2': writeHappyNumbersToFile()
    elif option == '3': fileOverlap()
    elif option == '0': break
    else : print("Invalid option!")
