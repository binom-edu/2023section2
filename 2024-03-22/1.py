# пузырьковая сортировка
n = int(input())
a = [int(i) for i in input().split()]

flag1 = False
for i in range(n):
    flag = False
    for j in range(n - 1, 0, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            flag = True
            flag1 = True
    if flag:
        print(*a)
    else:
        break
if not flag1:
    print(*a)