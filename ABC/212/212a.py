A,B = map(int,input().split())

if A>0 and B == 0:
    print("Gold")
if A>0 and B>0:
    print("Alloy")
if A==0 and B>0:
    print("Silver")