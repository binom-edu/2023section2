import random
fout = open('01', 'w')
fcor = open('01.a', 'w')

n = 2000
p = [i for i in range(1, n + 1)]
random.shuffle(p)
print(*p, file=fcor)
# n = 5
# p = [5, 2, 1, 3, 4]
a = []
for i in range(n):
    t = [(p[j], j) for j in range(i, n) if p[j] > p[i]]
    if t:
        a.append(min(t)[1] + 1)
    else:
        a.append(0)
print(n, file=fout)
print(*a, file=fout)