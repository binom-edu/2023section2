a, b = map(int, input().split())

while a * b != 0:
    if a > b:
        a %= b
    else:
        b %= a
print(a + b)