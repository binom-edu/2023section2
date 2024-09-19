n = int(input())
ans = n
while n != 0:
    if n > ans:
        ans = n
    n = int(input())

print(ans)