# сумма цифр
n = int(input())
n_copy = n

ans = 0
while n > 0:
    d = n % 10
    # что-то делаем с d
    ans += d
    n //= 10

n = n_copy
print('сумма цифр числа', n, 'равна', ans)