# 6. Write a program to iterate over lists strings and dictionaries using loops.

numbers = [10, 20, 30]
print("List:")
for num in numbers:
    print(num)

name = "Python"
print("String:")
for ch in name:
    print(ch)

student = {"name": "Rahul", "age": 20}
print("Dictionary:")
for key, value in student.items():
    print(key, ":", value)
