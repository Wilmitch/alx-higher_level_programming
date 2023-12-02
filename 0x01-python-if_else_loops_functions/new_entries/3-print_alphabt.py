#!/usr/bin/python3
#Prints ASCII Alphabet except letter q and e
for c in range(97, 123):
	if c != 101 and c != 113:
		print(chr(c), end='')
