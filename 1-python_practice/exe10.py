#!/usr/bin/python3
name = input("What's your name please? ")
for i in name:
    if 'a' <= i <= 'z':
        print(chr(ord(i) - 32))
    else:
        print(i)
