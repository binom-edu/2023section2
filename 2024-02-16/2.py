a = [i ** 2 for i in range(10)]
print(a)
b = [i for i in a if i % 10 == 6]
print(b)
c = [int(i) for i in input().split()]
print(*c)