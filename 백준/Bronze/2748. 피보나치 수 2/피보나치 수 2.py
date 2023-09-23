f = {0:0, 1:1}

def fibo(n):
    if n in f:
        return f[n]
    else:
        f[n] = fibo(n-1) + fibo(n-2)
        return f[n]
        

n = int(input())
print(fibo(n))