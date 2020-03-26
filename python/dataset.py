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

admins = {"Moose", "Joker", "Joker"}
moderators = {"Ann", "Chris", "Jane", "Moose", "Zero"}

print(admins) # This will auto deduplicate the extra Jokers
print("Joker" in admins) # Is joker an admin?
print("Joker" in moderators) # Is Joker a moderator?
print(admins | moderators) # admins, moderators and everyone work as both, aka, everyone form both lists
print(admins & moderators) # Who both is an admin and a moderator?
print(admins - moderators) # Who is admin but is not moderator?
print(admins ^ moderators) # Who has only one identity form these lists?
# using methods will make the code more homo-sapiens friendly and easier maintaince.
print(admins.union(moderators)) # same as |
print(admins.intersection(moderators)) # same as &
print(admins.difference(moderators)) # same as -
print(admins.symmetric_difference(moderators)) # same as ^

# upgrade a dataset
print()
arch = {"arm", "x86"}
print(arch)
arch.add("IA64")
print(arch)
arch.remove("arm")# This will delete an element if it exists in the target dataset. If it's not then it will return with KeyError
print(arch)
arch.discard("AMD64")# This will delete an element if it exists in the target dataset but it will continue even when the element is not in the target dataset
print(arch)
print(arch.pop())# This will delete the first element and return with its value. Apply it to an empty dataset will generate KeyError.
print(arch.clear())
Iarch = {"Atom", "Celeron", "Pentium", "Core", "Xeon"}
print(Iarch)
arch.update(Iarch)
print(arch)