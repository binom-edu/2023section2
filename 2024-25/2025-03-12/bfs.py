import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

q = []
INF = 10 ** 6
d = [INF] * n
d[0] = 0
q.append(0)

while q:
    v = q.pop(0)
    for u in g[v]:
        if d[u] == INF:
            d[u] = d[v] + 1
            q.append(u)
print(d)