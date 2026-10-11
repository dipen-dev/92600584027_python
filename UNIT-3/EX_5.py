# 5. Write a program to display current date and time using datetime module.

import datetime

now = datetime.datetime.now()
print("Current Date and Time :",now)

formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted Date and Time :",formatted_date)
