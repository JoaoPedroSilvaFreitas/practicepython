__author__ = 'joao'

from random import randint, seed

list_1 = [randint(1,20) for _ in range(randint(10, 15))]
list_2 = [randint(1,20) for _ in range(randint(10, 15))]
list_output = []

for i in range(0,len(list_1)):
    list_1[i] = randint(0,100)
    print(str(list_1[i]) + ", " , end='')
print()

for i in range(0,len(list_2)):
    list_2[i] = randint(0,100)
    print(str(list_2[i]) + ", ", end='')
print()

for i in range(0,len(list_1)):

    for j in range(0,len(list_2)):
        if list_1[i] == list_2[j] and list_output.count(list_1[i]) == 0: 
            print("ENCONTROU")
            list_output.append(list_1[i])

if len(list_output) != 0:
    for i in range(0,len(list_output)):
        print(str(list_output[i]) + ",", end='')

