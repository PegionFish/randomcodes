import random 
n = 3
a_list = [random.randrange(65, 91) for i in range(n)]
print(a_list)

# Insert
print()
a_list.insert(1, "Example 1")

# Remove
print()
print(a_list)
a_list.remove("Example 1")
print(a_list)

# Delete via pop() and return values that has been removed
print()
print(a_list)
p = a_list.pop(2)
print(a_list)
print(p)

# Difference between pop() and del, or remove()

print()
a_list.insert(2,"example")
a_list.insert(2,"example")
print(a_list)
del a_list[2]
print(a_list)

print()
print(a_list.remove("example"))
print(a_list)