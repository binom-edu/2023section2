n = int(input())
a = [int(i) for i in input().split()]

for i in range(3):
    idx = i
    for j in range(i, n):
        if a[j] < a[idx]:
            idx = j
    a.insert(i, a.pop(idx))

print(*a)