# 6. Write a program to perform file and directory operations using os and sys modules.
import os
import sys

print("Current Working Directory:", os.getcwd())

if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")
    print("Directory created successfully")

with open("MyFolder/test.txt", "w") as f:
    f.write("Welcome to Python Programming")

print("Files and Directories:", os.listdir("MyFolder"))

with open("MyFolder/test.txt", "r") as f:
    print("File Content:", f.read())

print("File Name:", os.path.basename("MyFolder/test.txt"))
print("Directory Name:", os.path.dirname("MyFolder/test.txt"))
print("Absolute Path:", os.path.abspath("MyFolder/test.txt"))
print("Is File:", os.path.isfile("MyFolder/test.txt"))
print("Is Directory:", os.path.isdir("MyFolder"))

print("Python Script Name:", sys.argv[0])

os.remove("MyFolder/test.txt")
print("File deleted successfully")

os.rmdir("MyFolder")
print("Directory deleted successfully")
