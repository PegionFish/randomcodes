import random

random = random.randrange(1,10000)

if random % 2 == 0:
    print(random, " is even")
else:
    print(random, "is odd")