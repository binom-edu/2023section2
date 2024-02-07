def f(n):
    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b

n = int(input())
print(f(n))