__author__ = 'joao'

str = input("String:")
n = len(str)-1
is_palindrome = True

##for i in range(0,len(str)):
    ##if str[i] != str[n]:
        ##is_palindrome = False
        ##break
    ##n -= 1

for i in str:
    if i != str[n]:
        is_palindrome = False
        break
    n -= 1

if is_palindrome:
    print("is palindrome")
else:
    print("isn`t palindrome")

