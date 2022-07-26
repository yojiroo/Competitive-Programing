N = int(input())
A = []
for i in range(N):
    a = input()
    A.append(a)
ans = True

for i in range(N):
    for j in range(N):
        if A[i][j] == "-":
            continue
        if A[i][j] == "W" and A[j][i] =="L":
            continue
        if A[i][j] == "L" and A[j][i] =="W":
            continue
        if A[i][j] == "D" and A[j][i] =="D":
            continue
        ans = False

if ans:
    print("correct")
else:
    print("incorrect")