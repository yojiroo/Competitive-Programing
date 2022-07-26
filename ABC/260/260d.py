N,K = map(int,input().split())
P = list(map(int,input().split()))

yama = [[0]for _ in range(N)]
ful = [False] * N
cnt = [0] * N
allm = 10**9
for i in range(N):
    for j in range(N):
        m = 10**9
        if yama[j] != [0]:
            m = yama[j][-1]
        if ful[j] == False and P[i] < m:
            yama[j].append(P[i])
            if len(yama[j]) == K+1:
                ful[j] = True
                for k in range (K):
                    idx = yama[j][k+1]
                    cnt[idx-1] = i+1
            break

for i in range(N):
    if cnt[i] == 0:
        print(-1)
    else:
        print(cnt[i])