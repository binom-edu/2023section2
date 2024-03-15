# пузырьковая сортировка
import random
n = 5
a = [random.randint(0, 20) for i in range(n)]
print(a)

for i in range(n):
    flag = False
    for j in range(n - 1, 0, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            flag = True
    print(*a)
    if not flag:
        break
