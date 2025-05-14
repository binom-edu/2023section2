n = int(input())
a = [int(i) for i in input().split()]
m = int(input())
b = [int(i) for i in input().split()]
x = a[0]
y = b[0]

i = j = 0
while i < n and j < m:
    while i < n and a[i] < b[j]:
        if abs(a[i] - b[j]) < abs(x - y):
            x, y = a[i], b[j]
        i += 1
    if i == n:
        break
    while j < m and b[j] <= a[i]:
        if abs(a[i] - b[j]) < abs(x - y):
            x, y = a[i], b[j]
        j += 1
print(x, y)