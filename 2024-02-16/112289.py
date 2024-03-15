n = int(input())
a = [int(i) for i in input().split()]
x = int(input())

ans = 0
for i in a:
    if i == x:
        ans += 1
print(ans)