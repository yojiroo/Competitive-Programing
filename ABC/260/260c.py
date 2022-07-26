n,x,y = map(int,input().split())

red = [0]*(n+1)
red[n] = 1  
blue = [0]*(n+1)

while n > 1:
    #red
    blue[n] += red[n] * x
    red[n-1] += red[n]
    red[n] = 0
    #blue
    red[n-1] += blue[n]
    blue[n-1] += blue[n] * y
    blue[n] = 0
    n -= 1

print(blue[1])
