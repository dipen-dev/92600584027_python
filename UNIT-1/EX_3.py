# 3. Write a program to perform arithmetic relational and logical operations using Python operators. 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nArithmetic Operations")
print("Addition of", a, "and", b, "is:", a + b)
print("Subtraction of", a, "and", b, "is:", a - b)
print("Multiplication of", a, "and", b, "is:", a * b)
print("Division of", a, "and", b, "is:", a / b)
print("Modulus of", a, "and", b, "is:", a % b)

print("\nRelational Operations")
print(a, ">", b, ":", a > b)
print(a, "<", b, ":", a < b)
print(a, "==", b, ":", a == b)
print(a, "!=", b, ":", a != b)
print(a, ">=", b, ":", a >= b)
print(a, "<=", b, ":", a <= b)

print("\nLogical Operations")
print(a, "> 0 and", b, "> 0:", a > 0 and b > 0)
print(a, "> 0 or", b, "> 0:", a > 0 or b > 0)
print("not(", a, ">", b, "):", not(a > b))