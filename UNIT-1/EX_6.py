# 6. Write a program to illustrate the use of tuples and sets with basic operations.

print("---Tuple---")
numbers = (10, 20, 30, 40)

print("Tuple:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Tuple length:", len(numbers))

print("\n---Set---")
set1 = {10, 20, 30, 40}

print("Set:", set1)

set1.add(50)
print("After adding 50:", set1)

set1.remove(20)
print("After removing 20:", set1)

set2 = {30, 40, 50}

print("Set 2:", set2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)