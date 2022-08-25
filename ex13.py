__author__ = 'joao'

def getFibonacci(fibonacci):
    fibonacci.append(fibonacci[len(fibonacci)-1] + fibonacci[len(fibonacci)-2])

number = int(input("number: "))

fibonacci = [0,1]

for i in range(1,number):
    getFibonacci(fibonacci)

print(*fibonacci)