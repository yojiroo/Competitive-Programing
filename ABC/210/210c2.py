N,K = map(int,input().split())
C = list(map(int,input().split()))

from collections import defaultdict
colors = defaultdict(int)

cnt = 0

#最初のK個
for i in range(K):
    colors[C[i]] += 1
    if colors[C[i]] == 1:
        cnt += 1

ans = cnt

#1ずつずらして確認
for i in range(1,N-K+1):
    colors[C[i-1]] -= 1
    if colors[C[i-1]] == 0:
        cnt -= 1
    colors[C[i+K-1]] += 1
    if colors[C[i+K-1]] == 1:
        cnt += 1
    ans = max(ans,cnt)
print(ans)
