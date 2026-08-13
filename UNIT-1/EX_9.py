# 9. Write a program to define and use of user-defined functions with different types of arguments.

print("Function with No Argument")
def hello():
    print("Hello Python")

hello()

print("\nFunction with Positional Arguments")
def add(a, b):
    print("Addition =", a + b)

add(10, 20)

print("\nFunction with Default Argument")
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Dipen")

print("\nFunction with Keyword Arguments")
def student(name, age):
    print("Name =", name)
    print("Age =", age)

student(age=20, name="Dipen")