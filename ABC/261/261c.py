N = int(input())
from collections import defaultdict
count=defaultdict(int)

for i in range(N):
    S = input()
    count[S] += 1
    if count[S] == 1:
        print(S)
    else:
        print(S+"(" + str(count[S]-1)+")")