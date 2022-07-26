h,w,n = map(int,input().split())
cards = []
gyou = []
retu = []
for i in range(n):
    a,b = map(int,input().split())
    cards.append([a,b])
    gyou.append(a)
    retu.append(b)

gyou = set(gyou)
gyou = list(gyou)
gyou.sort()

gyou_convert = dict()
for i in range(len(gyou)):
    gyou_convert[gyou[i]] = i+1

retu = set(retu)
retu = list(retu)
retu.sort()

retu_convert=dict()

for i in range(len(retu)):
    retu_convert[retu[i]] = i+1

for gyou,retu in cards:
    ans_gyou = gyou_convert[gyou]
    ans_retu = retu_convert[retu]
    print(ans_gyou,ans_retu)

