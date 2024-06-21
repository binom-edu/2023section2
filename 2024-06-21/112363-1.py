n, m = map(int, input().split())
a = []
for i in range(n):
    lst = [int(j) for j in input().split()]
    a.append(lst)

ans = 0
# for i in a:
#     for j in i:
#         ans += j

# for i in range(n):
#     for j in range(m):
#         ans += a[i][j]

# сумма элементов нулевой строки
for i in a[0]:
    ans += i
print(ans)

# сумма элементов нулевого столбца
ans = 0
for i in range(n):
    ans += a[i][0]
print(ans)

for i in a:
    print(*i)