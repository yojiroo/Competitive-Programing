N,M = map(int,input().split())
X = [0]+list(map(int,input().split()))
C = [0]*(N+1)

for i in range(M):
    c,y = map(int,input().split())
    C[c] = y

ans = 0
dp = [[-10**10]*(N+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(1,N+1):
    for j in range(N+1):
        now = -10**10
        if j == 0:
            for k in range(N+1):
                now = max(now,dp[i-1][k])
        else:
            now = dp[i-1][j-1]+X[i]+C[j]
        dp[i][j] = now

for i in range(N+1):
    ans = max(ans,dp[N][i])

print(ans)