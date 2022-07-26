a,b,c,d = map(int,input().split())

mizu = a
aka = 0
ans = 0
if b >= c*d:
    print(-1)
    exit()

while mizu > aka*d:
    mizu += b
    aka += c
    ans += 1

print(ans)
