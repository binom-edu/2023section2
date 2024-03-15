for _ in range(int(input())):
    a = [1] + [int(i) for i in input()]
    for i in range(5):
        if a[i] == 0:
            a[i] = 10
    ans = 4
    for i in range(1, 5):
        ans += abs(a[i] - a[i - 1])
    print(ans)
