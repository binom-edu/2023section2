a, b = map(int, input().split())
for i in range(a, b + 1):
    x = i
    while x > 0:
        d = x % 10
        if d == 0 or i % d != 0:
            break
        x //= 10
    else:
        print(i, end=' ')