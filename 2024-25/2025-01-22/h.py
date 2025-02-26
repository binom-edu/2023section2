import heapq

n, m = map(int, input().split())
a = [int(i) for i in input().split()]
x = []
y = []
for i in range(m):
    t1, t2 = map(int, input().split())
    x.append(t1)
    y.append(t2)

ans = []
q = [[0, j] for j in range(m)]
heapq.heapify(q)
for vis in a:
    t, j = heapq.heappop(q)
    ans.append(j + 1)
    heapq.heappush(q, [t + x[j] + vis * y[j], j])
while q:
    t, j = heapq.heappop(q)

print(t)
print(*ans)