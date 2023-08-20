# "윤년"이란 그레고리력에서 여분의 하루인 2월 29일을 추가하여 1년 동안 날짜의 수가 366일이 되는 해를 말한다.

def solution(a, b):
    if a==1:
        date = b
    elif a==2:
        date = 31+b
    elif a==3:
        date = 31+29+b
    elif a==4 or a==6 or a==8:
        date = (31+29) + 31*(a//2-1) + 30*(a//2-2) + b
    elif a==5 or a==7:
        date = (31+29) + 31*(a//2-1) + 30*(a//2-1) + b
    elif a==9 or a==11:
        date = (31+29) + 31*(a//2) + 30*(a//2-2) + b
    elif a==10 or a==12:
        date = (31+29) + 31*(a//2-1) + 30*(a//2-2) + b
        
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    answer = day[date%7]
    return answer