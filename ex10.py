__author__ = 'joao'

from random import randint, seed

list_1 = [randint(1,20) for _ in range(randint(10, 15))]
list_2 = [randint(1,20) for _ in range(randint(10, 15))]
list_output = []

for i in list_1: i = randint(0,100)
for i in list_2: i = randint(0,100)

print(*list_1)
print(*list_2)

list_output = [i for i in list_1 if (i in list_2) and (i not in list_output)]

print(*list_output)