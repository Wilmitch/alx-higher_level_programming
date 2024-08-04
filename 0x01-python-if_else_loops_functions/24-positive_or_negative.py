#!/usr/bin/python3
import random


number = random.randint(-10, 10)
if number < 0:
    print(f"The number is {number} and is negative")
elif number == 0:
    print("The number is zero")
else:
    print(f"The number is {number} and is positive")


