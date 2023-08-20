def solution(N, stages):
    failure_rate = {}
    
    users = len(stages)
    
    for i in range (1, N+1):
        if users==0:
            failure_rate[i] = 0
        else:
            challengers = stages.count(i)
            failure_rate[i] = challengers/users
            users = users - challengers
    
    return sorted(failure_rate, key=lambda x: failure_rate[x], reverse=True)

# 참고 : dictionary의 value 값을 정렬하기
# https://korbillgates.tistory.com/171 [생물정보학자의 블로그]
# https://programmers.co.kr/questions/15682