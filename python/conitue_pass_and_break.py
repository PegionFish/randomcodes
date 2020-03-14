# using contiue pass and break controlling flow while running
for n in range(2, 100):
    if n == 2:
        print(n)
        continue # start next loop ignoring all codes below
    for i in range(2, n):
        if (n % i) == 0:
            break # stops the loop & start another due to the first for
        else: # this beloings to the seconde for: when there is completely no break this else will be executed.
            print(n)