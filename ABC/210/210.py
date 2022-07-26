N = int(input())
S = "?"+input()

for i in range(1,N+1):
    if S[i] == "1":
        if i%2 == 1:
            print("Takahashi")
            exit()
        else:
            print("Aoki")
            exit()

