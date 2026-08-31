# 8. Write a program to illustrate variable scope using local global and nonlocal variables.

x = 10     
def outer():
    y = 20 
    def inner():
        nonlocal y
        y = 30
        print("Nonlocal:", y)
    inner()
    z = 40   
    print("Local:", z)
    
outer()
print("Global:", x)
