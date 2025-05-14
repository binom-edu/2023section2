import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
g = [dict() for i in range(n)]
for i in range(m):
    v, u, w = map(int, input().split())
    v -= 1
    u -= 1
    g[v][u] = w
print(g)

INF = 10 ** 9
d = [INF] * n
used = [False] * n
s = min_v = 0 # стартовая вершина
d[s] = 0
min_d = 0

while min_d != INF:
    used[min_v] = True
    for u in g[min_v]:
        if not used[u] and d[min_v] + g[min_v][u] < d[u]:
            d[u] = d[min_v] + g[min_v][u]
    # ищем мин. вершину среди не покрашенных
    min_d = INF
    for v in range(n):
        if not used[v] and d[v] < min_d:
            min_d = d[v]
            min_v = v
print(d)