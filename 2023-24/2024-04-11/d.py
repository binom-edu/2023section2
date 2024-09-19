for _ in range(int(input())):
    x = int(input())
    ans = 0
    d1 = 1
    while d1 < x:
        if x ** 2 % d1 == 0:
            d2 = x ** 2 // d1
            if (d2 - d1) % 2 == 0:
                ans += 1
        d1 += 1
    print(ans)