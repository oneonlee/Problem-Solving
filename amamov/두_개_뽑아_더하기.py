'''
https://programmers.co.kr/learn/courses/30/lessons/68644
'''

from itertools import combinations

def solution(numbers):
    result = list(set([sum(c) for c in combinations(numbers, 2)]))
    result.sort()
    return result

'''
def solution(numbers):
    result = []
    for idx, var1 in enumerate(numbers[:-1]):
        for var2 in numbers[idx+1:]:
        twosum = var1 + var2
            if not twosum in result:
               result.append(twosum)
    result.sort()
    return result
'''
