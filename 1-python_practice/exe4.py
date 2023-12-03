#!/usr/bin/python3
name = input("Hey beautiful, what's your name? ")
print(f"{name} is a such a beautiful name!")
name_len = input("Let's play a lil game. Guess how many letters your name has...\
Whoever gets it right gets cheered! So whats the answer? ")
if int(name_len) == len(name):
	print("Correct!!! Hooray! you're a genius!")
else:
	print("Please clap for me as you go back to your fomer school to claim your fees! Hahaa!\
Your name has {:d} letters.".format(len(name)))
print("Thank you for playing!")
greetings = input("And how do you say have a good day in your mother tongue? ")
print(f"{greetings} to you too!")
