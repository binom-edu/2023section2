def lower_bound(x):
    l, r = -1, n
    while r - l > 1:
        m = (r + l) // 2
        if a[m] < x:
            l = m
        else:
            r = m
    return r

n, k = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

for x in b:
    pos = lower_bound(x)
    if pos == n or a[pos] != x:
        print('NO')
    else:
        print('YES')