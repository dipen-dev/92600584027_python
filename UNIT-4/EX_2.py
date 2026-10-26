# 2. Write a program to demonstrate constructor and destructor usage.

class Car:
    def __init__(self, name):
        self.name = name
        print("Constructor: ",self.name," has been created.")

    def __del__(self):
        print("Destructor: ",self.name," has been destroyed.")

my_Car = Car("BMW")
del my_Car
