#!/usr/bin/python3
x = float(input("Enter the first addition number: "))
y = float(input("Enter the second addition number: "))
#addition
z = round(x + y)
print(z)

#if i needed to include separators for big numbers above 1000...
print(f"{z:,}") 
