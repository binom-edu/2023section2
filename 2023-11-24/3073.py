z = 0
ans = 0
while z != 2:
    n = int(input())
    ans += n
    if n == 0:
        z += 1
    else:
        z = 0
print(ans)