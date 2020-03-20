import random
n = 3

a_list = [random.randrange(65,91) for i in range(n)]
b_list = [chr(random.randrange(65,91)) for i in range(n)]
print(a_list)
print(b_list)
c_list = a_list + b_list + a_list * 2
print(c_list)
# Add a new element
c_list.append("100")
print(c_list)

# Clear a list
print()
print(a_list)
a_list.clear()
print(a_list)

# Copy a list
print()
d_list = c_list.copy()
print(d_list)
del d_list[6:8]
print(d_list)
print(c_list) # List C would make no change since all modifcation are adapted to d_list rather than C

# Difference between Copy and Assignment
print ()
e_list = d_list 
del e_list[6:8]
print(e_list)
print(d_list)
# I'm not sure why changes to assignmented lists affect to source. 

# Adding a list to exisistence list via extend
print()
print(a_list)
a_list.extend(c_list)
print(a_list)

# Insert an element to a list on demanded location
print()
print(a_list)
a_list.insert(1,"example_1")
a_list.insert(3,"example_3")
print(a_list)

# range
print()
print(a_list)
a_list.reverse()
print(a_list)
x = a_list.reverse()
print(x)

print("end")