L1,R1,L2,R2 = map(int,input().split())
r = min(R1,R2)
l = max(L1,L2)
if r > l:
    x = r-l
    print(x)
else:
    print(0)