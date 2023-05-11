def foo(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return foo(n-1) + foo(n-2) + foo(n-3)
    
num = int(input())

for _ in range(num):
    n = int(input())
    print(foo(n))