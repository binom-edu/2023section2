def f(x):
    ans = 0
    for i in a:
        ans += i // x
    return ans

n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

l = 0
r = max(a) + 1
while r - l > 1:
    m = (l + r) // 2
    if f(m) >= k:
        l = m
    else:
        r = m
print(l)