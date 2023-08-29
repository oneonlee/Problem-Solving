from itertools import permutations


def is_prime_num(num): # 3부터 max_n 이하의 수 들 중, 소수를 구하는 함수
    
    if num == 0 or num == 1:
        return False
    
    isPrime = True
    for i in range(2, num):
        if num%i == 0:
            isPrime = False
            break
            
    return isPrime




def solution(numbers):


    candidates = []
    for n_len in range(1, len(numbers)+1):
        result = list(permutations(numbers, n_len)) # [('1',), ('7',)] or [('1', '7'), ('7', '1')]
        
        for tup in result:
            str_num = ""
            for s in tup:
                str_num += s
            if int(str_num) not in candidates:
                candidates.append(int(str_num))
                
    answer = []
    for num in candidates:
        if is_prime_num(num)==True:
            answer.append(num)
#     answer = set(candidates).intersection(set(prime_list))
    print(answer)
    
    return len(answer)