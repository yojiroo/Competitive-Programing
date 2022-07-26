# 入力の受け取り
N,K=map(int, input().split())
a=list(map(int, input().split()))
 
# aをソートした数列
a_sort=sorted(a)
 
# 国民番号→順序(小さい方から何番目か)への変換
number_order=dict()
 
# i=0~(N-1)
for i in range(N):
    # 国民番号→順序への変換
    number_order[a_sort[i]]=i+1
 
# K÷Nの商
syou=K//N
# K÷Nの余り
amari=K%N
 
# i=0~(N-1)
for i in range(N):
    # 順序が(K÷Nの余り)以下なら
    if number_order[a[i]]<=amari:
        # 商+1を出力
        print(syou+1)
    # そうでないなら(順序が(K÷Nの余り)より大きいなら)
    else:
        # 商を出力
        print(syou)