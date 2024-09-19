def f(x):
    last = a[0]
    cnt = 1
    for i in a:
        if i - last >= x:
            last = i
            cnt += 1
    return cnt >= k


n, k = map(int, input().split())
a = [int(i) for i in input().split()]

l, r = 1, a[-1]
while r - l > 1:
    m = (r + l) // 2
    if f(m):
        l = m
    else:
        r = m
print(l)