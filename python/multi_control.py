for n in range (2, 100):
    if n == 2:
        print (n)
        continue
# Second loop
    for i in range (2, n):
        if (n % i) == 0:
            break
# This is else for the first loop
    else:
        print(n)