def decomp(n):
    sum = n
    for i in str(n):
        sum = sum+int(i)
    return sum
    
n = int(input())

flag = False
for i in range(1, n):
    if n==decomp(i):
        print(i)
        flag = True
        break

if flag==False:
    print(0)