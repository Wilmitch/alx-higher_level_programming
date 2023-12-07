#!/usr/bin/python3
'''
if age is 5 go to kindergarten
if age is 6 - 17, go to grades 1 through 12
if age is greater than 17 go to college
this to be done in less than 10 lines
'''
age = eval(input("Please enter the age: "))
if age < 5:
	print("Shouldnt be in school!")
if age == 5:
	print("Go to Kindergarten")
elif 6<= age <= 17:
	grade = age - 5
	print("Go to grade {}".format(grade))
elif age > 17:
	print("Go to college")
