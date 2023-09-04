# def solution(people, limit):
#     people.sort(reverse=True)
    
#     answer = 0
#     while True:
#         ############################################
#         boat = [0]
#         max_person = people[0]
#         r_weight = limit - max_person

#         for i in range(1, len(people)):
#             if r_weight < people[i]:
#                 pass
#             else: # r_weight >= people[i]:
#                 r_weight = r_weight - people[i]
#                 boat.append(i)
#                 if r_weight < 40:
#                     break

#         boat.sort(reverse=True)
#         for idx in boat:
#             del people[idx]
#         ############################################
#         answer+=1
        
#         if len(people)==0:
#             break
    
    
    
    
#     return answer


def solution(people, limit):
    cnt = 0
    people.sort()
    '''
    무거운놈 넣고
    남은놈중에 맞는놈있나 확인해야함
    '''
    people.sort(key=lambda x:-x)
    # print(people)

    left=0
    right=len(people)-1
    rest=limit
    while left<=right:
        #처음에 제일 무거운 놈 넣기
        rest-=people[left]
        left+=1
        #가벼운 놈들 다 넣기
        if rest>=people[right]:
            # print(people[right])
            rest-=people[right]
            right-=1
        # print(left,right)
        cnt+=1
        rest=limit



    return cnt