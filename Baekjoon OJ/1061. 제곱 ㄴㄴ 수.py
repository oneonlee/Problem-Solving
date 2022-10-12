import math

def foo(N):
    if N<4:
        return True
        
    sqrt = int(math.sqrt(N)) 
    for num in range(2, sqrt+1):
        if N%math.pow(num, 2) == 0:
            # print(N, math.pow(num, 2))
            return False
    return True

a, b = input().split()
a = int(a)
b = int(b)


square_number = [int(math.pow(num, 2)) for num in range(int(math.sqrt(a)), int(math.sqrt(b)) + 1)]

print(square_number)
cnt = 0


for i in range(a, b+1):
    if foo(i)==True:
        # print(i)
        cnt+=1
print(cnt)
