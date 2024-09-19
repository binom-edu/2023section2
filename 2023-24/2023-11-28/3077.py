n = int(input())
ans = 1
cur = 1
while n != 0:
    prev = n
    n = int(input())
    if n == prev:
        cur += 1
        ans = max(ans, cur)
    else:
        cur = 1
print(ans)
