#!/usr/bin/python3
#Ask user for their name.
name = input("What's your name? ")

#assuming they included unnecessary spaces in it, we can remove the whitespaces by.
name = name.strip()
print(name)

#assuming we needed to capitalize the first letter of their name we would...
name = name.capitalize()
print(name)

#assuming we needed to capitalize every first letter of each word, we would...
name = name.title()
print(name)

#assuming the user input two names and we needed to greet them by only the first name...
first, last = name.split(" ")
print(f"hello, {first}") 
