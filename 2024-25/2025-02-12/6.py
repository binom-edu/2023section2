n, k = map(int, input().split())
a = [int(i) for i in input().split()]


ans = 0

if k == 2:
    s1, s2 = 0, sum(a)
    for i in range(n - 1):
        s1 += a[i]
        s2 -= a[i]
        ans = max(ans, abs(s2 - s1))
else:
    mpre = [a[0]]
    for i in range(1, n):
        mpre.append(min(mpre[-1], a[i]))
    msuf = [0] * n
    msuf[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        msuf[i] = min(msuf[i + 1], a[i])
    cur = sum(a[:n - k + 1])
    ans = abs(cur - msuf[n - k + 1])
    for i in range(k - 1):
        cur -= a[i]
        cur += a[n - k + i + 1]
        if i < k - 2:
            ans = max(ans, abs(cur - mpre[i]), abs(cur - msuf[n - k + i + 2]))
        else:
            ans = max(ans, abs(cur - mpre[i]))
print(ans)