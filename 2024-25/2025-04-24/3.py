n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a.sort()
b.sort()
l, t = map(int, input().split())
for i in range(m):
    b[i] += t
i = j = ans = 0
while i < n and j < m:
    while i < n and b[j] - a[i] > l:
        i += 1
    if i == n: break
    while j < m and b[j] - a[i] <= l:
        ans = max(ans, b[j] - a[i])
        j += 1
print(max(ans - 2 * t, 0))