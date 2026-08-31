# 9. Write a program to demonstrate iterators and iterables in Python.

num = [10, 20, 30, 40, 50, 60]
print(num)
print("Iterable: ")
for i in num:
    print(i)
print("Iterable: ")
num_iter = iter(num)
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
