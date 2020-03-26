import os # This is for deleting file.
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
g.close()

# Read different lines of a given file
h = open("test-file.txt", "r")
print(h.readline()) # add .strip can remove "\n" but I'm not sure what's the difference
print()
print(h.readline())
print()
print(h.readline())
h.close()

# Read a given file as a list
print()
i = open("test-file.txt", "r")
LIST = i.readlines() # Using upper letter is because "list" is already been taken by Python.
print(LIST)
i.close

# Iterate the list
print()
for line in LIST:
    print(line)
i.close

# Writing to a file from a list
print()
cpu_list = ["Intel Core i9 9900KS\n", "AMD Ryzen 9 3950X\n", "Qualcomm Snapdragon 835\n"]
WRITE = open("test-file.txt", "w")
WRITE.writelines(cpu_list)
WRITE.close()

READ = open("test-file.txt", "r")
for line in READ.readlines():
    print(line)
READ.close()

# Deleting the file
print()
delete = open("test-file.txt", "w")
print(f"{delete.name} will be deleted")
delete.close()
if os.path.exists(delete.name):
    os.remove(delete.name)
    print(f"{delete.name} has been deleted")
else:
    print(f"{delete.name} is not exist")

# Special Purpose Block for files - with
print()
with open('test-file.txt', "w") as FILE:
    FILE.write("草你妈\n三天之内杀了你\n把你骨灰都扬了")

with open("test-file.txt", "r") as FILE:
    for line in FILE.readlines():
        print(line)

if os.path.exists(FILE.name):
    os.remove(FILE.name)
    print(f"{FILE.name} has been deleted")
else:
    print(f"{FILE.name} does not exist.")