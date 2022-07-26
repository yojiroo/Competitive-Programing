n,x,y,z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

gokaku = [False]*n
sugaku = {}
eigo = {}
total = {}

for i in range(n):
    sugaku[i] = A[i]
    eigo[i] = B[i]
    total[i] = A[i]+B[i]

sugaku2 = sorted(sugaku.items(), key=lambda x:x[1], reverse=True)


for i in range(x):
    idx = sugaku2[i][0]
    gokaku[idx] = True
    del eigo[idx]
    del total[idx]

eigo2 = sorted(eigo.items(), key=lambda x:x[1], reverse=True)

for i in range(y):
    idx = eigo2[i][0]
    gokaku[idx] = True
    del total[idx]

total2 = sorted(total.items(), key=lambda x:x[1], reverse=True)
for i in range(z):
    idx = total2[i][0]
    gokaku[idx] = True

for i in range(n):
    if gokaku[i] == True:
        print(i+1)