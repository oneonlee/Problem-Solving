def making_resukt_list(L, max_num):
    if max_num>3:
        for n in range(4, max_num+1):
            L[n] = L[n-1] + L[n-2] + L[n-3]
    return L
    
L = [False for _ in range(11)]

L[1] = 1
L[2] = 2
L[3] = 4


    
num = int(input())

in_list = []

for _ in range(num):
    n = int(input())
    in_list.append(n)
    
making_resukt_list(L, max(in_list))

for n in in_list:
    print(L[n])