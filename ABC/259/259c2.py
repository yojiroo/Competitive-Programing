s = input()
t = input()

from itertools import groupby

def runLengthEncode(S: str) -> "list[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

sr = runLengthEncode(s)
tr = runLengthEncode(t)
ans = True

if len(sr) != len(tr):
    print("No")
    exit()

for i in range (len(sr)):
    if sr[i][0] != tr[i][0]:
        ans = False
    if sr[i][1] > tr[i][1]:
        ans = False
    if sr[i][1] == 1 and tr[i][1] >= 2:
        ans = False

if ans:
    print("Yes")
else:
    print("No")