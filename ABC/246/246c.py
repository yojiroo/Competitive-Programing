n,k,x = map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
af = []
for a in A:
    t = a//x
    if t > 0:
        a = a-x*t
        cnt += t
    '''while で回すと tle なので、x で割った商を使う方法で行う
        if a > x:
        while a >= x:
            a = a-x
            cnt += 1
    '''
    af.append(a)
ans = 0
if cnt >= k:
    ans = sum(A) - k*x
    print(ans)
    exit()
else:
    k -= cnt
    af.sort(reverse=True)
    if len(af) <= k:
        print(0)
        exit()
    for i in range(k):
        af[i] = 0
print(sum(af))

