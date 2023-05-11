import math

def making_trinum_list(L, max_num):
    for n in range(1, max_num+1):
        L[n] = int(n*(n+1)/2)
    return L
    
def foo(n):
    x = int(math.sqrt(2*n-15/4)-0.5)
    for i in L[1:x+1]:
        for j in L[1:x+1]:
            for k in L[1:x+1]:
                if i+j+k == n:
                    return 1
    return 0

num = int(input())

input_list = []
for _ in range(num):
    n = int(input())
    input_list.append(n)
    
L = [False for _ in range(max(input_list)+1)]
L = making_trinum_list(L, max(input_list))

for n in input_list:
    print(foo(n))