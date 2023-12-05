#!/usr/bin/python3
def hello(to = "World"):
	print("Hello,", to)

#if we need to give our parameters a default value if not provided by the user...
#we use a equal sign to assign our parameter name to our default value

#main
hello()
name = input("What's your name? ")
hello(name)
