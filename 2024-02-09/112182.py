def f(n):
    if n == 0:
        return
    f(n // 2)
    print(n % 2, end='')

n = int(input())
if n == 0:
    print(0)
    exit(0)
if n < 0:
    n *= -1
    print('-', end='')
f(n)