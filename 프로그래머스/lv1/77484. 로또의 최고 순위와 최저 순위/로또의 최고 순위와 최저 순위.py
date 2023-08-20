def solution(lottos, win_nums):
    unknown_nums = lottos.count(0) # lottos의 포함된 0의 개수
    
    for i in range (0, unknown_nums): 
        lottos.remove(0)
    
    # 남은 lottos의 번호 중, 몇 개의 번호가 일치하는지 계산
    same_nums = 0
    for num in lottos:
        for win in win_nums:
            if (num == win):
                same_nums += 1
    
    # 최고 순위와 최저 순위를 계산
    max_rank = 7 - (same_nums + unknown_nums)
    min_rank = 7 - same_nums
    
    # 순위는 6등보다 낮을 수 없으므로 6등보다 낮다면 6등으로 고정해준다.
    if min_rank > 6:
        min_rank = 6
        if max_rank > 6:
            max_rank = 6
            
    # answes에 대입
    answer = []
    answer.append(max_rank)
    answer.append(min_rank)
    
    return answer