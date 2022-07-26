S = input()
n = len(S)
mod = 10**9+ 7
goal = "chokudai"
dp = [[0] * 9 for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1

for i in range(n):
    for j in range(8):
        dp[i+1][j+1] = dp[i][j+1]
        if S[i] == goal[j]:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= mod

print(dp[n][8])
