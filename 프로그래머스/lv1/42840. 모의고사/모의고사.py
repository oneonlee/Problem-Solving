import math # 올림을 하기 위해 사용

def solution(answers):
    number_of_questions = len(answers) # 주어진 문제의 개수
    
    # 문제 수보다 넉넉하게 losers의 답들의 list를 만듬
    loser_1 = [1, 2, 3, 4, 5] * math.ceil(number_of_questions/5)
    loser_2 = [2, 1, 2, 3, 2, 4, 2, 5] * math.ceil(number_of_questions/8)
    loser_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * math.ceil(number_of_questions/10)
    
    score_of_loser_1 = 0
    score_of_loser_2 = 0
    score_of_loser_3 = 0
    
    for question_num in range(0, number_of_questions):
        if (loser_1[question_num] == answers[question_num]):
            score_of_loser_1 += 1
        if (loser_2[question_num] == answers[question_num]):
            score_of_loser_2 += 1
        if (loser_3[question_num] == answers[question_num]):
            score_of_loser_3 += 1

    losers_score = [score_of_loser_1, score_of_loser_2, score_of_loser_3]
    highest_score = max(losers_score)
    
    winner_of_losers = []    
    if(score_of_loser_1 == highest_score):
        winner_of_losers.append(1)
    if(score_of_loser_2 == highest_score):
        winner_of_losers.append(2)
    if(score_of_loser_3 == highest_score):
        winner_of_losers.append(3)    
    
    return winner_of_losers

# 참고 : 내장함수-max https://wikidocs.net/32#max
# 참고 : 반올림, 내림, 올림 https://wikidocs.net/21113