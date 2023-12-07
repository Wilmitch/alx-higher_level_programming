#!/usr/bin/python3
#get height of tree
tree = eval(input("Enter the height of your xmas tree: "))

#starting spaces
init_space = tree - 1

#hashes
hash = 1

#save stump space
stump_space = tree - 1

#loop the right number of times while printing the tree
while tree != 0:
	for i in range(init_space):
		print(' ', end = "")
	for i in range(hash):
		print('#', end = "")
	print()
	init_space -= 1
	hash += 2
	tree -= 1
for i in range(stump_space):
	print(" ", end = '')
print("#")


