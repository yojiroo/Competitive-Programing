S = input()

count = 0

for num in range(10000):
    OK = True
    num = str(num)
    # 0 埋め 4 桁
    num = num.zfill(4)

    for i in range(10):
        if S[i] == "o":
            if str(i) not in num:
                OK = False
        if S[i] == "x":
            if str(i) in num:
                OK = False
    
    if OK == True:
        count += 1

print(count)