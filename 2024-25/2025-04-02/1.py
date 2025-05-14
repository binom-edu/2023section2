import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        for u, t in g[v]:
            vote_next = (ans[v] - 1 + t) % 2
            if ans[u] == -1:
                ans[u] = vote_next + 1
                q.append(u)
            elif ans[u] != vote_next + 1:
                print('NO')
                exit(0)

n, m = map(int, input().split())
g = []
for i in range(n):
    g.append([])
for i in range(m):
    x, y, t = (int(j) - 1 for j in input().split())
    g[x].append([y, t])
    g[y].append([x, t])
ans = [-1] * n

res = True
for v in range(n):
    if ans[v] == -1:
        ans[v] = 1
        bfs(v)
else:
    print('YES')
    print(*ans)