n, m = map(int, input().split())
a = []
for i in range(n):
    lst = [int(j) for j in input().split()]
    a.append(lst)

ans = 0
# for i in a:
#     for j in i:
#         ans += j

for i in range(n):
    for j in range(m):
        ans += a[i][j]

print(ans)