for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    a[0] += 1
    ans = 1
    for i in a:
        ans *= i
    print(ans)