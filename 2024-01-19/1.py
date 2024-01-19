import random
n = 10
a = [random.randint(0, 20) for i in range(n)]
print(a)

print('a[1:4]', a[1:4])
print('a[:4]', a[:4])
print('a[1:]', a[1:])
print('a[::]', a[::])
print('a[::-1]', a[::-1])