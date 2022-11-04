def check(n):
    if n<100:
        return True
    else:
        a=n%10
        n=n//10
        b=n%10
        
        
        diff=b-a
        
        
        while True:
            b=n%10
            n=n//10
            c=n%10
            if n<10 and c==0:
                return True
            if c-b!=diff:
                return False


N = int(input())

cnt=0
for i in range(1, N+1):
    
    if check(i):
        cnt+=1
            
print(cnt)