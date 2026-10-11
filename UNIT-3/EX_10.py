# 10.Write a program to extract specific information from a text file using regular expressions. 
import os
import re

with open("data.txt", "w") as f:
    f.write("Name: Jalpin\nAge: 21\nEmail: jalpin@gmail.com\nPhone: 9876543210\n")

with open("data.txt", "r") as f:
    text = f.read()

name = re.findall(r"Name:\s*(.*)", text)
age = re.findall(r"Age:\s*(\d+)", text)
email = re.findall(r"Email:\s*([\w.-]+@[\w.-]+)", text)
phone = re.findall(r"Phone:\s*(\d+)", text)

print("Name:", name[0])
print("Age:", age[0])
print("Email:", email[0])
print("Phone:", phone[0])

os.remove("data.txt")
print("Test File deleted successfully")
