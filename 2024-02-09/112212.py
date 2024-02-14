def f(n):
    if n == 0:
        return 0
    d = (n % 2 + 1) % 2
    return d + f(n // 10)

print(f(int(input())))