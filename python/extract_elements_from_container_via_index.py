import random

n = 3
# 65-91 is larger English notes in UNICODE
a_list = [random.randrange(65, 91) for i in range (n)]
b_list = [chr(random.randrange(65, 91)) for i in range (n)]
print (a_list)

c_list = a_list + b_list + a_list * 2
print (c_list)

print()
# Extract via Index, aka slicing
print(c_list[3]) # Output element with Index 3
print(c_list[:]) # Output element from allthe list
print(c_list[5:]) # Output element starting from Index 5 to the end
print(c_list[:3]) # Output element before Index 3
print(c_list[2:6]) # Output element from Index 2 to 6

print()
# Delete via Index
del c_list[3]
print(c_list)
del c_list[5:8]
print(c_list)

print()
# Swap via Index
c_list[1:5:2] = ["a", 2] # [start:stop:step], much like range

print(c_list)