# Output Successione di Fiboncaci under 1000

n = 1000
a, b = 0, 1

while a < n:
    print (a, end=" ")
    a, b = b, a + b
print()