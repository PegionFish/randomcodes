# diciionary is mapped by _key_ and _value_
phonebook = {"ann":1234, "bob":2234, "copper":3234, "dunce":4234}
print(phonebook)

# Generate an empty dicitionay
print()
aDict = {}
print(aDict)

# using key as index can get value
print()
print(phonebook["bob"])

# key will be the only in the same dictionay. If there is a repeated key, it will be automaticlly deduplicated.
print()
phonebook = {"ann":1234, "bob":2234, "copper":3234, "dunce":4234, "ann":1234}
print(phonebook) # This will not output the last ann

# Upgrade a certain element
print()
print(phonebook)
phonebook["dunce"] = 6666
print(phonebook)
print(phonebook["dunce"])

# Add elements to a dict from an exsisting dict
print()
phonebook2 = {"clearlove":4396, "xiaohu":2200, "baolan":4397}
print(phonebook2)
phonebook.update(phonebook2)
print(phonebook)

# Delete an element from existing dict
print()
del phonebook["ann"]
print(phonebook)

# Logical Operator
print()
print("ann" in phonebook)
print("bob" in phonebook.keys())
print(4396 in phonebook.values())
print(("clearlove", 4396) in phonebook.items())

# Build-in Functions avaliable for manipulation
print()
print(len(phonebook)) # The length of the dict
print(max(phonebook)) # Outputs the largest key
print(min(phonebook)) # Outputs the minimal key
print(list(phonebook))
print(tuple(phonebook))
print(set(phonebook))
print(sorted(phonebook))
print(sorted(phonebook, reverse=True))

# Common methods
print()
# Copying will make a new copy for the original dict
phonebook3 = phonebook.copy()
print(phonebook3)
# Clearing the copy would not effect the original one
phonebook3.clear()
print(phonebook3)
print(phonebook)
# .popitem removes the item that was last inserted into the dictinoay
print()
p = phonebook.popitem()
print (p)
print(phonebook)
# .pop removes the specified item. Keyname is required but the defaultvalue is optional
print()
p = phonebook.pop("clearlove", 4396)
print (p)
print(phonebook)
# .get returns the value of the item with the specified key. Keyname is required, but the value is optional
print()
p = phonebook.get("baolan", 4397)
print (p)
print(phonebook)
# .setdefault returns the value of the item with the specified key. If the key doesnt exist, insert the key with the specified value.
print()
p = phonebook.setdefault("xiaohu", 2200)
print(p)
print(phonebook)
