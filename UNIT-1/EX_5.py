# 5. Write a program to create and manipulate lists using indexing slicing and list comprehensions. 

numbers = [10, 20, 30, 40, 50]

print("List =", numbers)
print("First element =", numbers[0])
print("Last element =", numbers[-1])
print("Slicing =", numbers[1:4])

numbers.append(60)
print("After adding 60 =", numbers)

numbers.remove(20)
print("After removing 20 =", numbers)

square = [x * x for x in numbers]
print("Square of numbers =", square)
