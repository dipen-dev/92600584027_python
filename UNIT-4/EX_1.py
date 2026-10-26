# 1.Write a program to create a class and object in Python. 

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print("Car brand : ",self.brand)
        print("Car Model : ",self.model)
        print("Car Year : ",self.year)

my_car = Car("Toyota", "Corolla", 2023)
my_car.display_info()
