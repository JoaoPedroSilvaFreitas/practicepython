__author__ = 'joao'

def maxOfThree(x,y,z):
    max = -float("inf")
    if x > max: max = x
    if y > max: max = y
    if z > max: max = z
    return max

print("Max of three numbers: ")
x = float(input("X:"))
y = float(input("Y:"))
z = float(input("Z:"))

print("Max of x y and z: " + str(maxOfThree(x,y,z)))