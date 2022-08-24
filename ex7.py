__author__ = 'joao'

from random import randint, seed

list = [randint(1,20) for _ in range(randint(10, 15))]
output = []

for i in list:
    i = randint(0,100)

for i in list:
    print(str(i) + ", " , end='')
print()

output = [i for i in list if i % 2 != 0]

##for i in list: 
##    if i % 2 != 0:
##        output.append(i)

for i in output:
    print(str(i) + ", " , end='')
print()