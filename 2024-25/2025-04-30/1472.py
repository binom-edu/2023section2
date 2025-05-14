# 4 5
# 0 0 0 0 1
# 0 1 1 0 2
# 0 2 1 0 0
# 0 0 1 0 0

from collections import deque

n, m = map(int, input().split())
g = []
for i in range(n):
    g.append([int(j) for j in input().split()])

d = [[-1 for j in range(m)] for j in range(n)]
d[0][0] = 0
q = deque()
q.append((0, 0))
while q:
    i, j = q.popleft()
    for di, dj in (-1, 0), (1, 0), (0, 1), (0, -1):
        i1, j1 = i, j
        while 0 <= i1 < n and 0 <= j1 < m:
            if g[i1][j1] == 2:
                print(d[i][j] + 1)
                exit(0)
            elif g[i1][j1] == 1:
                i1 -= di
                j1 -= dj
                if d[i1][j1] == -1:
                    d[i1][j1] = d[i][j] + 1
                    q.append((i1, j1))
                break
            i1 += di
            j1 += dj
        else:
            i1 -= di
            j1 -= dj
            if d[i1][j1] == -1: 
                d[i1][j1] = d[i][j] + 1
                q.append((i1, j1))