n,m,x,t,d = map(int,input().split())

if x <= m <= n:
    print(t)
    exit()
if m <= x:
    sintyo = t-(x-m)*d
    print(sintyo)