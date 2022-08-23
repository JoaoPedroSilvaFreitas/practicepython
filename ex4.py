__author__ = 'joao'

num = int(input("num:"))

for i in range(1,num + 1):
    if num % i == 0:
        print("é divisível por " + str(i))