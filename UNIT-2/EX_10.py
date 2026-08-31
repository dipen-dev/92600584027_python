# 10. Write a program to generate a sequence of numbers using generator functions and yield keyword. 

def generator(n):
    for i in range(1,n+1):
        yield i

n = int(input("Enter the number: "))
print("Sequence: ", end="")
for num in generator(n):
    print(num, end=" ")
