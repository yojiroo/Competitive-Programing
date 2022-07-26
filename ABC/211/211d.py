# 入力の読み込み
N,M=map(int,input().split())
connect =[[] for _ in range(N+1)]
for i in range(M):
	A,B=map(int,input().split())
	connect[A].append(B)
	connect[B].append(A)
mod = 10**9 + 7

inf = 10**15

time = [inf] * (N+1)
time[1] = 0

count=[0]*(N+1)

count[1] = 1

from collections import deque
que = deque()

que.append(1)

while 0<len(que):
    now_city = que.popleft()

    for to_city in connect[now_city]:
        if time[to_city] == inf:
            count[to_city]=count[now_city]
            time[to_city] = time[now_city]+1
            que.append(to_city)
        else:
            if time[to_city] == time[now_city] + 1:
                count[to_city] += count[now_city]
        count[to_city]%=mod

if time[N] == inf:
    print(0)
else:
    print(count[N])
