n = int(input())

d = 2
while d ** 2 <= n:
    if n % d == 0:
        print(d)
        break
    d += 1
else:
    print(n)