# 9. Write a program to read and write data into a file using different file modes. 

import os

with open("file1.txt", "w") as file:
    file.write("Line 1: Hello World\nLine 2: Python File Handling\n")

print("--- 1.Reading File ---")
with open("file1.txt", "r") as file:
    content = file.read()
    print(content)

print("--- 2.Appending File ---")
with open("file1.txt", "a") as file:
    file.write("Line 3: Line Three is Appended\n")

with open("file1.txt", "r") as file:
    print(file.read())

print("--- 3.Reading and Writing ---")
with open("file1.txt", "r+") as file:
    content = file.read()
    print("Original Content before r+:")
    print(content)
    file.write("Line 4: Added via r+\n")

with open("file1.txt", "r") as file:
    print("Final File Content:")
    print(file.read())

os.remove("file1.txt")
print("File deleted successfully")
