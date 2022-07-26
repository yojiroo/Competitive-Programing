N = int(input())
A = list(map(int,input().split()))
d = {}
for i in range (1,N+1):
    d[A[i-1]] = i
d2 = sorted(d.items())
print(d2[-2][1])