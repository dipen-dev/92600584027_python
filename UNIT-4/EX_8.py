# 8.Write a program to demonstrate encapsulation and abstraction using classes.

from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def get_balance(self, entered_pin):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

class BankAcc(Bank):
    def __init__(self, owner, initial_balance, pin):
        self.owner = owner
        self.__balance = initial_balance  
        self.__pin = pin                  

    # abstract method
    def get_balance(self, entered_pin):
        if entered_pin == self.__pin:
            return f"Your balance: {self.__balance}"
        else:
            return "PIN wrong!"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} successfully deposited")
        else:
            print("Some error, not deposited")


acc = BankAcc("Dipen", 5000, 1234)
print("ACCOUNT HOLDER:", acc.owner)

print("\n--- USING ABSTRACTION ---")
# Using the methods defined by the abstract interface
print(acc.get_balance(1234))
print(acc.get_balance(9999))

print("\n--- PROVING ENCAPSULATION WORKS ---")
acc.deposit(2000)
print(acc.get_balance(1234))
