x = int(input()) * 100
p = int(input())
y = int(input()) * 100

ans = 0
while x < y:
    ans += 1
    x += x * p // 100

print(ans)