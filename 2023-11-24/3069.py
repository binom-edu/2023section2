n = int(input())
prev = n + 1
ans = 0
while n != 0:
    if n > prev:
        ans += 1
    prev = n
    n = int(input())
print(ans)