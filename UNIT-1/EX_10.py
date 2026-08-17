# 10.Write a program to demonstrate recursion using factorial or Fibonacci series.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number: "))

result = factorial(n)
print("Factorial =", result)