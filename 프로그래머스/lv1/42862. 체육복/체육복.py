def solution(n, lost, reserve):
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))

    
    able = n - len(lost)
    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
            able += 1
            continue
        elif r+1 in lost:
            lost.remove(r+1)
            able += 1
            continue
    
    answer = able
    return answer

























# def solution(n, lost, reserve):
    
#     lost = list(set(lost)-set(reserve)) # 잃어버린 사람들 중, 여분이 있는 사람은 제외
#     reservse = list(set(reserve)-set(lost))
    
#     # possesion = n - len(lost) # 빌려주기 전, 체육복을 가지고 있는 사람
#     print("lost", lost)
#     print("reserve", reserve)
    
    
#     # for loser_num in lost:
#     #     for reserver_num in reserve:
#     #         print(loser_num, reserver_num)
#     #         if abs(loser_num - reserver_num) == 1:
#     #             loser_num = 100
#     #             reserver_num = 200
#     #             print("lost", lost)
#     #             print("reserve", reserve)
#     #             break
                
#     for i in range (0, len(lost)):
#         for j in range (0, len(reserve)):
#             print(lost[i], reserve[j])
#             if abs(lost[i] - reserve[j]) == 1:
#                 lost[i] = 100
#                 reserve[j] = 200
#                 print("lost", lost)
#                 print("reserve", reserve)
            
                
#     try:
#         while True : lost.remove(100)
#     except ValueError:
#         pass
    
#     answer = n - len(lost)
#     return answer