# 5. Write a program to demonstrate the use of break continue and pass statements.

print("----- Break -----")
for i in range(1,6):
    if i==3:
        break
    print(i)
print("----- Continue -----")
for i in range(1,6):
    if i==4:
        continue
    print(i)
print("----- Pass -----")
for i in range(1,6):
    if i==4:
        pass
    print(i)
