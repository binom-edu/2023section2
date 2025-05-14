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

INF = 10 ** 6
d = [INF] * n
d[0] = 0
for dst in range(n):
    for v in range(n):
        if d[v] == dst:
            for u in g[v]:
                if d[u] == INF:
                    d[u] = dst + 1
print(d)