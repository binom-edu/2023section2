a = int(input())
b = int(input())
c = int(input())
d = int(input())

a, b, c = sorted([a, b, c])
dif = abs(c - a - b)
if dif > d:
    print(dif - d)
else:
    print(0)