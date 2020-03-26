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
    
# Multi Flow Control , using contiue pass and break controlling flow while running

print()

for n in range(2, 100):
    if n == 2:
        print(n)
        continue # start next loop ignoring all codes below
## This is second loop
    for i in range(2, n):
        if(n % i) == 0:
            break # stops the loop & start another due to the first for
    else: # this beloings to the seconde for: when there is completely no break this else will be executed.
        print(n)

# While 
# This program outputs Successione di Fiboncaci under 1000

print()

count = 1000
a, b = 0, 1

while a < count:
    print (a, end = "")
    a, b = b, a + b
print()

# For

print()

words = ["cats", "dogs", "pegionfish", "cyberpunk1919"]

for w in words:
    print (w, len(w))
