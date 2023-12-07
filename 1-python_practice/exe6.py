#!/usr/bin/python3
#ask user to enter miles to be converted to kilometers
miles = input("Please provide number of miles to be converted into kilometers ")

#convert the input into a float
miles = float(miles)

kilos = miles * 1.60934
print("{} miles equals {} kilometers".format(miles, kilos))
