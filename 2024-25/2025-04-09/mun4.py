import sys
sys.stdin = open('01')
fout = open('ans', 'w')
n = int(input())
a = [int(i) for i in input().split()]
pc = [i for i in range(1, n + 1)]
ans = [0] * n
for i in range(n):
    if a[i] == 0:
        ans[i] = pc.pop()
cur = max(a)
while cur > 0:
    for i in range(n):
        if a[i] == cur:
            ans[i] = pc.pop()
    cur -= 1
print(*ans, file=fout)