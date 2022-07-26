import heapq
hque = []
heapq.heapify(hque)

Q = int(input())
plus = [0]*(Q+1)
cum_plus=[0]*(Q+1)

for i in range(1,Q+1):
    q = list(map(int,input().split()))
    if q[0] == 1:
        X = q[1]
        minus=cum_plus[i-1]
        heapq.heappush(hque,[X-minus,i,minus])
        plus[i] = 0
        cum_plus[i] = cum_plus[i-1]+plus[i]
    elif q[0] == 2:
        X = q[1]
        plus[i] = X
        cum_plus[i] = cum_plus[i-1]+plus[i]
    else:
        num,k,minus = heapq.heappop(hque)
        ad = cum_plus[i-1] - cum_plus[k-1]
        print(num+minus+ad)
        plus[i] = 0
        cum_plus[i] = cum_plus[i-1]+plus[i]
