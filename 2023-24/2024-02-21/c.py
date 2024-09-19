for _ in range(int(input())):
    ans = ''
    for i in range(8):
        for c in input():
            if c != '.':
                ans += c
    print(ans)