def solution(a, b):
    answer = 0
    for i in range(0,len(a)):
        answer = answer+a[i]*b[i]
    return answer