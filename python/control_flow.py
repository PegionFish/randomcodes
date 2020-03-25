# Standard if-else mode

import random

random = random.randrange(1,10000)

if random % 2 == 0:
    print(random, " is even")
else:
    print(random, "is odd")

# If-elif-else mode

print()

x = int(input("Please input a interger:"))

if x < 0:
    x = 0
    print("Negative changed to zero.")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print ("More")
    
# Multi Flow Control

print()

for n in range(2, 100):
    if n == 2:
        print(n)
        continue
## This is second loop
    for i in range(2, n):
        if(n % i) == 0:
            break
## This else is for "if n == 2"
    else:
        print(n)