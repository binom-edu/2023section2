# сколько чисел на отрезке [a, b] имеют сумму цифр c

def check(n):
    global cnt
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    if ans == c:
        cnt += 1


a, b, c = map(int, input().split())
cnt = 0

for x in range(a, b + 1):
    check(x)
print(cnt)