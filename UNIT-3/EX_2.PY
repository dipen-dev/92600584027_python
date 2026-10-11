# 2. Write a program to demonstrate different import mechanisms in Python.

# Imports the entire module.
import EX_1_module

sum_result = EX_1_module.add(10, 5)
product_result = EX_1_module.multiply(4, 3)

print("1.Imports the entire module.")
print("Addition Result:", sum_result)
print("Multiplication Result:", product_result)

# Renames the module or item to a shorter or cleaner nickname.
import EX_1_module as cal

sum_result = cal.add(10, 5)
product_result = cal.multiply(4, 3)

print()
print("2.Renames the module or item to a shorter or cleaner nickname.")
print("Addition Result:", sum_result)
print("Multiplication Result:", product_result)

# Imports only the specified functions
from EX_1_module import add

sum_result = add(10, 5)

print()
print("3.Imports only the specified functions")
print("Addition Result:", sum_result)

# Imports EVERYTHING from the module directly
from EX_1_module import *

sum_result = add(10, 5)
product_result = multiply(4, 3)

print()
print("4.Imports EVERYTHING from the module directly")
print("Addition Result:", sum_result)
print("Multiplication Result:", product_result)
