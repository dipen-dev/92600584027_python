# 7. Write a program to create a dictionary and demonstrate dictionary methods and iteration.

# 7. Program to demonstrate dictionary methods and iteration

student = {
    "name": "Dipen",
    "age": 20,
    "course": "python"
}

print("Dictionary =", student)
print("Name =", student["name"])

student["age"] = 21
print("Updated age =", student["age"])

student["city"] = "Bhuj"
print("After adding city =", student)

student.pop("course")
print("After removing course =", student)

print("\nIteration:")
for key in student:
    print(key, "=", student[key])