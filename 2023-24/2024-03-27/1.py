import random

def isSorted():
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            return False
    return True

def f(l, r):
    if l >= r:
        return
    x = a[random.randint(l, r)]
    i = l
    j = r
    while i <= j:
        while i < r and a[i] < x:
            i += 1
        while j > l and a[j] > x:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    f(l, j)
    f(i, r)

n = 20
a = [random.randint(-1000, 1000) for i in range(n)]
print(a)
l = 0
r = len(a) - 1
f(l, r)
print(a)
print(isSorted())