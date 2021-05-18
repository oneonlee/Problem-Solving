def filter_loser(stages, cur_stage):
    a, b = 0, 0
    for stage in stages:
        if stage >= cur_stage:
            b += 1
        if stage == cur_stage:
            a += 1
    return a, b

def solution(N, stages):
    result = {}
    for cur_stage in range(1, N+1):
        a, b = filter_loser(stages, cur_stage)
        if b == 0:
            result[cur_stage] = 0
        else:
            result[cur_stage] = a / b
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    print(result)
    return [int(r[0]) for r in result]
