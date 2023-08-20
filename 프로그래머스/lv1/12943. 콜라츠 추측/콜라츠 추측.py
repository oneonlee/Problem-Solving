def solution(num):
    times = 0
    while times<500:
        if num==1:
            break
            
        if num%2 == 0:
            num = num/2
        else:
            num = num*3 + 1
        times += 1
            
    else:
        times = -1
        
    return times