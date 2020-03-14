# basic, range(5) means range(0, 5, 1)
for i in range(5):
    print(i)
print("-----------------------------------------")
# entended, range(1, 10) means range(1, 10, 1)
for j in range (1, 10):
    print(j)
print("-----------------------------------------")
# standard, range(1, 10, 2) means itself
for k in range(1, 10, 2):
    print(k)
print("-----------------------------------------")
# negetave works fine as well
for l in range (1, -10, -1):
    print(l)
print("-----------------------------------------")
# generate list
m = list(range(0, 100, 1))
print(m)
print("-----------------------------------------")