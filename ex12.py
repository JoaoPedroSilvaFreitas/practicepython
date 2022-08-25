__author__ = 'joao'

from random import randint, seed

list = [randint(1,20) for _ in range(randint(10, 15))]

list = [randint(1,20) for i in list]

print(*list)

output = [list[0], list[-1]]

print(*output)