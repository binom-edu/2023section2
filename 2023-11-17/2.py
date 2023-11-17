# дано число. определить, является ли оно простым
n = int(input())
d = 2
if n == 1:
    print('NO')
    exit(0)

while d < n:
    if n % d == 0:
        print('NO')
        break
    d += 1
else:
    print('YES')