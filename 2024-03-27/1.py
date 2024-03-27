import random

a = [1, 13, 19, 6, 18, 9, 6, 5]
print(a)
l = 0
r = len(a) - 1
x = a[random.randint(l, r)]
print(x)

i = l
j = r
while i < j:
    while i < r and a[i] < x:
        i += 1
    while j > l and a[j] > x:
        j -= 1
    if i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

print(a)
print(i, j)