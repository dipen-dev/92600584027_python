# 6. Write a program to illustrate the use of tuples and sets with basic operations.

# Tuple
t = (10, 20, 30, 40)

print("Tuple =", t)
print("First element =", t[0])
print("Tuple length =", len(t))

# Set
s1 = {10, 20, 30, 40}
print("Set S1 =", s1)

s1.add(50)
print("After add (50) =", s1)

s1.remove(20)
print("After remove (20) =", s1)

s2 = {30, 40, 50}
print("Set S2 =", s2)

print("Union of (s1 | s2) =", s1 | s2)
print("Intersection of (s1 & s2)  =", s1 & s2)