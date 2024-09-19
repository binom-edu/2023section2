n = int(input())
m = n
cnt = 0
while n > 0:
    cnt += 1
    n //= 10

cnt -= 1
while cnt >= 0:
    print(m // 10**cnt % 10, end=' ')
    cnt -= 1
