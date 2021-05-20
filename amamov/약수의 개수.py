def divisor_cnt(num):
    result = 0
    for n in range(1, num+1):
        if num % n == 0:
            result += 1
    return result

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        div = divisor_cnt(num)
        if div % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer
