#!/usr/bin/python3
#ask user for two integers and store them separately
num1, num2 = input("Please input two numbers ").split()
#convert the strings into regular numbers
num1 = int(num1)
num2 = int(num2)

#addition
sum = num1 + num2

#subtraction
difference = num1 - num2

#product
product = num1 * num2

#quotient
quotient = num1 / num2


#remainder
remainder = num1 % num2

#print results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))

