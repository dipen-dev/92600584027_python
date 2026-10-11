# 3. Write a program to perform mathematical operations using math module.

import math

print("----- 1. Basic Arithmetic & Rounding Operations -----")
print("Ceiling of 4.2:", math.ceil(4.2))
print("Floor of 4.8:", math.floor(4.8))
print("Absolute value of -7.5:", math.fabs(-7.5))
print("Factorial of 5:", math.factorial(5))
print()

print("----- 2. Power & Roots -----")
print("Square root of 64:", math.sqrt(64))
print("3 raised to the power of 4:", math.pow(3, 4))
print()

print("=== 3. Constants & Trigonometry -----")
print("Value of Pi (π):", math.pi)
print("Value of Euler's number (e):", math.e)

angle_degrees = 45
angle_radians = math.radians(angle_degrees)

print(f"Sine of {angle_degrees}°:", math.sin(angle_radians))
print(f"Cosine of {angle_degrees}°:", math.cos(angle_radians))
print()

print("----- 4. Logarithmic Functions -----")
print("Logarithm of 100 to base 10:", math.log(100, 10))
print("Logarithm of 16 to base 2:", math.log2(16))
print("Natural logarithm of e:", math.log(math.e))
