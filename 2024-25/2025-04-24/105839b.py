a, b, p = map(int, input().split())
c, d, q = map(int, input().split())

if a == 0 and c == 0:
    if p * d == b * q:
        print('Ambiguity')
    else:
        print('Contradiction')
elif b == 0 and d == 0:
    if p * c == a * q:
        print('Ambiguity')
    else:
        print('Contradiction')
elif a == 0:
    y = p / b
    