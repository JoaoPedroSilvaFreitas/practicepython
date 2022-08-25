__author__ = 'joao'

number = int(input("number:"))

divisors = [i for i in range(1,number + 1) if number % i == 0]

print("Prime" if len(divisors) <= 2 else "Not prime")