for _ in range(int(input())):
    n = int(input())
    ans = 2
    best = 0
    for x in range(2, n + 1):
        k = n // x
        if x * (k + 1) * k // 2 > best:
            best = x * (k + 1) * k // 2
            ans = x
    print(ans)