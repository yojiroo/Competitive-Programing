s = list(input())
s.reverse()
for i in range(len(s)):
    if s[i] == '9':
        s[i] = '6'
        continue
    if s[i] == '6':
        s[i] = '9'
s = "".join(s)
print(s)