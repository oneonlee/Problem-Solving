def grading():
    sheet = input()
    
    cnt = 0
    score = 0
    for char in sheet:
        if char=='O':
            cnt+=1
            score+=cnt
        else:
            cnt=0

    return score

N = int(input())

for _ in range(N):
    print(grading())