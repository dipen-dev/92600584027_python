# 8. Write a program to explain mutable and immutable objects in Python.

print("Mutable object - List") 
a = [10, 20, 30]

print("Before:", a)

a[0] = 100

print("After:", a)

print("Immutable object - Tuple")
b = (10, 20, 30)

print("Tuple:", b)

print("b[0] = 100 This will give an error") 