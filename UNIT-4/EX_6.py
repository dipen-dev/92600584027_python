class Payment:
    def pay(self, amount):
         print("Processing payment:", amount)

class UPI(Payment):
     def pay(self, amount):
            print("Payment of Rs.", amount, "done using UPI")   

class CreditCard(Payment):
     def pay(self, amount):
          print("Payment of Rs.", amount, "done using Credit Card")

# POLYMORPHISM: Calling the same method name on different objects
p1 = UPI()
p1.pay(5000)

p2 = CreditCard()
p2.pay(500)   
