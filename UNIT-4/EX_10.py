# 10.Write a program to perform file pointer operations using seek and tell methods. 

import os

with open("pointer_demo.txt", "w") as file:
    file.write("abcdefghijklmnopqrstuvwxyz")

with open("pointer_demo.txt", "r") as file:
    print("Initial pointer position:",file.tell())
    
    data1 = file.read(5)
    print("Read 5 characters:",data1)
    print("Pointer position after read:",file.tell())
    
    file.seek(10)
    print("Pointer moved to position:",file.tell())
    
    data2 = file.read(4)
    print("Read 4 characters from new position:",data2)
    print("Pointer position now:",file.tell())
    
    file.seek(0)
    print("Pointer reset to beginning:",file.tell())
    print("Read first character:",file.read(1))

os.remove("pointer_demo.txt")
print("File deleted successfully")
