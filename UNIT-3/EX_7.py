# 7. Write a program to copy move and delete files using shutil module.
import shutil
import os

if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")
    print("Directory created successfully")

with open("test.txt", "w") as f:
    f.write("Welcome to Python Programming")

shutil.copy("test.txt", "copy.txt")
print("File copied successfully")

shutil.move("copy.txt", "MyFolder/copy.txt")
print("File moved successfully")

os.remove("MyFolder/copy.txt")
print("Copy File deleted successfully")

os.remove("test.txt")
print("Test File deleted successfully")

os.rmdir("MyFolder")
print("Directory deleted successfully")
