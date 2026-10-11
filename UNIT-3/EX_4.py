# 4. Write a program to generate random numbers using random module.

import random

r_float = random.random()
print("Random float number between 0 and 1:",r_float)

r_int = random.randint(1,10)
print("Random integer number between 1 and 100:",r_int)

r_uniform = random.uniform(2.3,6.5)
print("Random float number between 2.3 and 6.5:",r_uniform)
