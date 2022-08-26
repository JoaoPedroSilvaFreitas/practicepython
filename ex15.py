__author__ = 'joao'

## Resolução em uma linha do site
def reverseWord(w):
  return ' '.join(w.split()[::-1])


def reverseString(str):
    list = str.split()
    j = len(list) - 1

    for i in range(0,j):
        if i > j: break
        aux = list[i]
        list[i] = list[j]
        list[j] = aux
        j -= 1

    str = " ".join(list)
    return str


str = input("string: ")
str = reverseString(str)
print("reversed: " + str)