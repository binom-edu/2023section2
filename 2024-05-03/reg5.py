def f(x):
    ans = 0
    for z, a, b in engines:
        if x <= z:
            ans += a * x
        else:
            ans += a * z + b * (x - z)
    return ans

n, p = map(int, input().split())
engines = []
for i in range(n):
    engines.append([int(j) for j in input().split()])

l, r = 1, 10 ** 12
while r - l > 1:
    m = (r + l) // 2
    if f(m) < p:
        l = m
    else:
        r = m
print(r)