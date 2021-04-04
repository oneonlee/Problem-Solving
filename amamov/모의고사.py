def one_generator():
    while True:
        for i in [1, 2, 3, 4, 5]:
            yield i

def two_generator():
    while True:
        for i in [2, 1, 2, 3, 2, 4, 2, 5]:
            yield i

def three_generator():
    while True:
        for i in [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]:
            yield i

def solution(answers):
    result = []
    score_one, score_two, score_three = 0, 0, 0
    one, two, three = one_generator(), two_generator(), three_generator()
    for answer in answers:
        if answer == next(one):
            score_one += 1
        if answer == next(two):
            score_two += 1
        if answer == next(three):
            score_three += 1
    scores = [score_one, score_two, score_three]
    max_score = max(scores)
    for idx, score in enumerate(scores):
        if max_score == score:
            result.append(idx + 1)
    
    return result
