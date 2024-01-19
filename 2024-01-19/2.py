import random
n = 10
a = [random.randint(0, 20) for i in range(n)]
print(a)

x = a.pop()
print(a)
print(x)

a.pop(4)
print(a)

for i in range(10, 20):
    if i in a:
        a.remove(i)

print(a)

a.insert(1, 33)
print(a)

# циклический сдвиг вправо:
a.insert(0, a.pop())
print(a)