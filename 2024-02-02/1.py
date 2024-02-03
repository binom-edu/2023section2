def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input())
y = int(input())

print(gcd(x, y))