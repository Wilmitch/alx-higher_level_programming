#!/usr/bin/python3
x = int(input("Please enter an integer: "))
if x < 0:
	x = 0
	print("Negative converted to zero")
elif x == 0:
	print("Zero")
elif x == 1:
	print("single")
else:
	print("more")
