s = input()

tmp,count,ans = s[0],1,""
for i in range(1,len(s)):
    if s[i] == tmp:
        count += 1
    else:
        ans += tmp+str(count)
        tmp = s[i]
        count = 1
ans += tmp + str(count)

print(ans)
