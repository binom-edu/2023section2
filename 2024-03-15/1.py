# сортировка выбором
import random
n = 5
a = [random.randint(0, 20) for i in range(n)]
print(a)

for i in range(n - 1):
    idx = i
    for j in range(i, n):
        if a[j] < a[idx]:
            idx = j
    a[i], a[idx] = a[idx], a[i]
print(a)