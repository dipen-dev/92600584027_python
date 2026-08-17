# 8. Write a program to explain mutable and immutable objects in Python.

print("---Mutable Object (List)---")

numbers = [10, 20, 30]

print("Before modification:", numbers)

numbers[0] = 100

print("After modification:", numbers)


print("\n---Immutable Object (Tuple)---")

values = (10, 20, 30)

print("Tuple:", values)
print("Tuple elements cannot be modified.")