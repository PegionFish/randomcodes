# How to generate a tuple
a = 1, 2, 3 # Working but not recommend
b = (1, 2, 3) # It's recommended

print(a)
print(b)
print(a == b)  # a and b are the same tuple thus the result is True

# Never leave without comma

print()

a = 2, # This is a tuple,the comma after made that fact.
print(a)

b = 2 # This is not
print(b)

c = (2) # This is not too
print(c)

d = (2,) # This is a tuple
print(d)

print(a == d) 

# "Add" another element at the end of a tuple
# Add is quoted because the modified tuple is in fact not the same tuple as before which can be seen via id

print()

a = (1,)
print(a)
print(id(a))
a += (3, 5,)
print(a)
print(id(a))

# Difference between List and Tuple

print()

number = 10000
alpha = range(number)
beta = tuple(alpha) # This move converted Alpha to tuple
charlie = list(alpha) # This move converted Alpha to list

# sizeof returns binary numbers

print(a.__sizeof__())
print(b.__sizeof__())
print(c.__sizeof__())