import random
n = 3

# Generate 3 random numbers & build a list
a_list = [random.randrange(65,91) for i in range(n)]
b_list = [chr(random.randrange(65,91)) for i in range(n)]
print(a_list)
print(b_list)

# List can be operated with + and *
c_list = a_list + b_list + a_list * 2
print(c_list)

a_list *= 3
print(a_list)

# Build-in function operation len(),max(),min()
print(len(c_list)) # Length of a list
print(max(b_list)) # Largest unit in list
print(min(b_list)) # Smallest unit in list

print("X" not in b_list)