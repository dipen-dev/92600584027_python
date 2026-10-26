# 3. Write a program to illustrate instance variables and class variables.

class Student:
    school_name = "Global High School"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

student1 = Student("Alice", 101)
student2 = Student("Bob", 102)

print(Student.school_name)
print(student1.name)
print(student1.roll_no)
print(student2.name)
print(student2.roll_no)

Student.school_name = "International Academy"
print(student1.school_name)
print(student2.school_name)
