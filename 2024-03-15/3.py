# пузырьковая сортировка
n = int(input())
a = [int(i) for i in input().split()]

flag = 0
for i in range(n):
    for j in range(n - 1, 0, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            flag = 2
    if flag < 2:
        break
    print(*a)
    flag = 1
if flag == 0:
    print(*a)
