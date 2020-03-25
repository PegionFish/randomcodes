# Generate a set
primes = {2, 3, 5, 7, 11, 13, 17}
print(primes)

# Generate a empty set
print()

a = {} # This will generate a dict rather than a set
b = set() # This will generate a empty set

print(type(a))
print(type(b))

# Casting from data list to set. Do notice the set returns has been deduplicated
print()

a = "abcdfejioajigunaunxnsaig"
b = range(10)
c = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 4, 5, 1, 4]
d = ("a", "b", "e", "b", "a")

print(set(a))
print(set(b))
print(set(c))
print(set(d))

# Operating a set
# Please notice that due to the fact that elements in sets are not indexed so del() will not function
print()

admins = {"Moose", "Joker", "Jokers"}
moderators = {"Ann", "Chris", "Jane", "Moose", "Zero"}

print(admins) # This will auto deduplicate the extra Jokers
print("Joker" in admins)
print("Joker" in moderators)
print(admins | moderators)