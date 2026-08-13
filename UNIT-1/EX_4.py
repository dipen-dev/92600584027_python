# 4. Write a program to demonstrate string operations including slicing formatting and built-in string functions. 

text = input("Enter a string: ")

print("\nString Operations")
print("Original String:", text)
print("First character:", text[0])
print("Last character:", text[-1])
print("String Slicing:", text[0:5])

print("\nString Formatting")
name = "Dipen"
age = 20
print("My name is", name, "and my age is", age)

print("\nBuilt-in String Functions")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
print("Replace:", text.replace("a", "A"))
print("Count of 'a':", text.count("a"))