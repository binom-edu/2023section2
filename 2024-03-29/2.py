n = int(input())
a = [int(i) for i in input().split()]
b = a.copy()
for i in range(n):
    b[i] %= 10

for i in range(n):
    for j in range(n - 1, 0, -1):
        if b[j] < b[j - 1]:
            b[j], b[j - 1] = b[j - 1], b[j]
            a[j], a[j - 1] = a[j - 1], a[j]
print(*a)