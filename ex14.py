__author__ = 'joao'

def removeDuplicates(list):
    output = []
    for i in list:
        if output.count(i) == 0:
            output.append(i)
    return output

def removeDuplicatesSet(list):
    newSet = set()
    for i in list:
        newSet.add(i)
    return newSet


from random import randint, seed

list = [randint(1,20) for _ in range(randint(10, 15))]
list = [randint(1,20) for i in list]

##output = removeDuplicates(list)
output = removeDuplicatesSet(list)

print(*list)
print(*output)
