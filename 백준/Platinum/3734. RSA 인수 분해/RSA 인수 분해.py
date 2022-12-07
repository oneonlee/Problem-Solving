import math
    
n, k = input().split()
n = int(n)
k = int(k)

# x = q-kp
for x in range(-100000, 100001):
    D = x*x + 4*k*n
    if D>=0:
        root_D = math.isqrt(D)
        if root_D*root_D != D:
            continue
        if (-x+root_D) % (2*k) == 0:
            p = (-x+root_D) // (2*k)
            q = n//p
            if n==p*q and p>1 and q>1:
                print(f"{int(min(p,q))} * {int(max(p,q))}")
                break

        if (-x-root_D) % (2*k) == 0:
            p = (-x-root_D) // (2*k)
            q = n//p
            if n==p*q and p>1 and q>1:
                print(f"{int(min(p,q))} * {int(max(p,q))}")
                break
        