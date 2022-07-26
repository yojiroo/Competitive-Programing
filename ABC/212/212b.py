X = input()


if X[0] == X[1] == X[2] == X[3]:
    print("Weak")
    exit()

num2 = (int(X[0])+1)%10
num3 = (int(X[1])+1)%10
num4 = (int(X[2])+1)%10

if int(X[1]) == num2 and int(X[2]) == num3 and int(X[3]) == num4:
    print("Weak")
else:
    print("Strong")


