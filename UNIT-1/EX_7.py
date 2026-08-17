# 7. Write a program to create a dictionary and demonstrate dictionary methods and iteration.

student = {
    "name": "Dipen",
    "age": 20,
    "course": "Python"
}

print("---Dictionary---")
print("Student:", student)

print("Name:", student["name"])

student["age"] = 21
print("Updated age:", student["age"])

student["city"] = "Bhuj"
print("After adding city:", student)

student.pop("course")
print("After removing course:", student)
print("\n---Iteration---")
for key, value in student.items():
    print(key, "=", value)
