#Defineing a function "is_prime" which can tell if a number is prime or not.
def is_prime (n):
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range (2, int(n ** 0.5) + 1):
        if (n % m) == 0:
            return False
    else:
        return True
#Start calling this function
for i in range(80,110):
    if is_prime(i):
        print(i)