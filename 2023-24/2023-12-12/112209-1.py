a, b = map(int, input().split())
for i in range(a, b + 1):
    x = i
    success = True
    while x > 0:
        d = x % 10
        if d == 0 or i % d != 0:
            success = False
        x //= 10
    if success:
        print(i, end=' ')