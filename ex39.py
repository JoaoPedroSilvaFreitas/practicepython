__author__ = 'joao'

import datetime

#reescrever o ex anterior usando o lib datetime do python...

name = input("Name:")
age = int(input("Age:"))
year = 100 - age + datetime.datetime.now().year
print(f"{name} in {year} you will be 100 years young!")

for i in range(0,int(input("Repeat:"))): 
        print(f"{name} in {year} you will be 100 years young!")
