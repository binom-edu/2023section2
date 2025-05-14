n = int(input())
b = [int(i) for i in input().split()]
b.sort()
a = [b[i + 1] - b[i] for i in range(n - 1)]

inf = 10 ** 9
dp = [[inf for j in range(n - 1)] for i in range(2)]
dp[1][0] = a[0]

for j in range(n - 2):
    dp[0][j + 1] = dp[1][j]
    dp[1][j + 1] = min(dp[0][j] + a[j + 1], dp[1][j] + a[j + 1])
print(dp[1][-1])