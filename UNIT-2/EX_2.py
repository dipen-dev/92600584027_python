# 2. Write a program to check whether a number is positive negative or zero using nested conditions.

num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Number is Zero")
    else:
        print("Number is Positive")
else:
    print("Number is Negative")