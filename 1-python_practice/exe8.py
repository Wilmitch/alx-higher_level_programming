#!/usr/bin/python3
'''
have the user enter their investment amount, and expected interest
each year their investment will increase by their investment + their investment x interest rate
print to them their earnings after a 10 year period
'''
init = float(input("Please enter the invested amount: "))
intrate = float(input("Please enter the offered interest rate: "))
for i in range(10):
	init = init + (init * (intrate/100))
print("Your total earnings after a 10 year period are: {:.2f}".format(init))

