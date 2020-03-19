import random

n = 10
a_list = [random.randrange(1, 100) for i in range (n)]
print(f"a_list conprehends {len(a_list)} random numbers:\n", a_list)

a_list.sort()
print("the list sorted:\n", a_list)

a_list.sort(reverse=True)
print("The list sorted reversely:\n", a_list)