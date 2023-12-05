#!/usr/bin/python3
x = float(input("What's the first number? "))
y = float(input("What's the second number? "))
z = x / y
print(z)

#to round off to the nearest whole number...
z = round(x / y, 2)
print(z)

#another way to round off using the format string
z = x / y
print(f"{z:.2f}")
