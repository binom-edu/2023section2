import random
n = 10
a = [random.randint(1, 100) for i in range(n)]
print(a)

for i in range(n):
    print(a[i])

for i in a:
    print(i)