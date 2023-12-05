#!/usr/bin/python3
def print_last_digit(number):
	string = str(number)
	last_number = string[-1]
	print(f"{last_number}", end = '')
	return last_number
