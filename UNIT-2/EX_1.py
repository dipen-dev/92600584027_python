# 1. Write a program to demonstrate conditional statements using if if-else and if-elif-else.

print("----- if statment -----")
age = int(input("Enter your age: "))
if age > 18:
    print("you are eligible to vote.")
print()
print("----- if else statment -----")
num = int(input("Enter any number: "))
if num % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")
print()
print("----- if-elif-else statment -----")
marks = int(input("Enetr any markas: "))
if marks > 90:
    print("Grade A")
elif marks > 75:
    print("Grade B")
elif marks > 50:
    print("Grade c")
elif marks > 33:
    print("Grade D")
else:
    print("Fail")
