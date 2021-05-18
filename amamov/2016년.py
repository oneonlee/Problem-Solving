def solution(month, day):
    month_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day = sum(month_day[:month]) + day
    if total_day % 7 == 1:
        return 'FRI'
    elif total_day % 7 == 2:
        return 'SAT'
    elif total_day % 7 == 3:
        return 'SUN'
    elif total_day % 7 == 4:
        return 'MON'
    elif total_day % 7 == 5:
        return 'TUE'
    elif total_day % 7 == 6:
        return 'WED'
    elif total_day % 7 == 0:
        return 'THU'
