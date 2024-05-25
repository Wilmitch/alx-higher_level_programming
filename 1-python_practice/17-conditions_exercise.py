#!/usr/bin/python3
name = input("Enter your name: ")
if len(name) < 3:
    print("Name must be at least 3 Characters")
elif len(name) > 50:
    print("Name cannot be above 50 characters")
else:
    print("Name looks good")

