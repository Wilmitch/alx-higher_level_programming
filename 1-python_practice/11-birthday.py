#!/usr/bin/python3
#receive age of user and advise them if their birthday is important or not.
age = int(input("Please enter the age "))

if 1 <= age <= 18:
	print("The birthday is important")
elif age == 21 or age == 50:
	print("It is important")
elif age > 65:
	print("Very important")
else:
	print("The birthday is not important!") 
