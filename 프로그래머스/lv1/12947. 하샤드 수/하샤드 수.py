def solution(x):
    sum_of_digits = x//10000 + (x % 10000)//1000 + (x % 10000 % 1000)//100 + (x % 10000 % 1000 % 100)//10 + (x % 10000 % 1000 % 100 % 10)//1
    if x%sum_of_digits == 0:      
        answer = True
    else:
        answer = False
    return answer