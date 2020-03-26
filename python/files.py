# Creating a file
open("test-file.txt", 'w') # The default mode is r which is read only, reverting to w means rebuild this file, and in this case is to generate this file.

# Saving file object into a variable for better use
f = open("test-file.txt", "w")
print(f.name)

# Read & Write to a given file
print()
f.write("This is Python\nOne Of the best programming languages out there\nThis is written by Pegionfish\n")
f.close()

g = open('test-file.txt', 'r')
s = g.read()
print(s)

# Read different lines of a given file
print(g.readline(1))

# Read a given file as a list
