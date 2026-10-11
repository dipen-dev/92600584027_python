# 8. Write a program to demonstrate basic regular expression pattern matching.
import re

text = "Welcome to Python Programming"

pattern = "Welcome"

result = re.search(pattern, text)

if result:
    print("Pattern found")
    print("Matched text:", result.group())
else:
    print("Pattern not found")
