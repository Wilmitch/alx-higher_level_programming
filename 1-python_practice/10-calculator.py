#!/usr/bin/python3
#gets input for a calculation from a user
num1, operator, num2 = input("Please enter a calculation ").split()

#convert the above strings into integers
num1 = float(num1)
num2 = float(num2)

#check what operator was passed in and give the necesarry output
if operator == '+':
	print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == '-':
	print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == '*':
	print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == '/':
	print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
	print("Only use either of these operators; +, -, *, /")
