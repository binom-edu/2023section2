def f(i):
    if i < 1: return 10 ** 9
    if dp[i] != 0: return dp[i]
    ans = min(f(i - 1), f(i - 5), f(i - 6)) + 1
    dp[i] = ans
    return ans

n = int(input())
dp = [0] * max(7, n + 1)
dp[1] = dp[5] = dp[6] = 1
print(f(n))
ans = []
cur = n
while cur > 0:
    if dp[cur - 1] == dp[cur] - 1:
        ans.append(1)
        cur -= 1
    elif dp[cur - 5] == dp[cur] - 1:
        ans.append(5)
        cur -= 5
    else:
        ans.append(6)
        cur -= 6

print(*ans[::-1])