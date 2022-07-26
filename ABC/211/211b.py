from collections import defaultdict
hits = defaultdict(int)

for i in range(4):
    s = input()
    hits[s] += 1

S = ["H","2B","3B","HR"]

ans = True
for s in S:
    if hits[s] == 1:
        continue
    else:
        ans = False

if ans:
    print("Yes")
else:
    print("No")
