def f():
    print('* ' * n) # глобальные переменные можно использовать
    x = 5666 # локальная переменная живет только внутри функции

n = 3 # глобальная переменная
f()
n = 5
f()
print(n)