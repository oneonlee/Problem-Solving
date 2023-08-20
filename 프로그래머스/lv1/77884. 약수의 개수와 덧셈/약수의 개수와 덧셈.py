def solution(left, right):
    answer = 0
    
    for n in range(left, right + 1):
        factors = []
        count = 0
        
        f=1
        while (f*f <= n):
            if n%f == 0:
                factors.append(f)
                if f*f != n:
                    factors.append(n//f)
                else:
                    break
            f+=1
        if len(factors)%2 == 0:
            answer += n
        else:
            answer -= n
        
    return answer