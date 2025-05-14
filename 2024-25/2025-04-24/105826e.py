from collections import Counter
s = input()
n = len(s)
f = Counter(s)
if len(f) == 1:
    print(0)
    print(s)
    exit(0)
a = sorted(f, key=lambda x: f[x], reverse=True)
if n % 2 == 0:
    x, y = f[a[0]], f[a[1]]
    v1 = n - x
    v2 = n - x - y
    if x > n // 2:
        v2 += x - n // 2
    if v1 < v2:
        print(v1)
        print(a[0] * n)
    else:
        print(v2)
        print((a[0] + a[1]) * (n // 2))
else:
    print(n - f[a[0]])
    print(a[0] * n)