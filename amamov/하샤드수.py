def solution(x):
    total = sum(int(i) for i in list(str(x)))
    if x % total == 0:
        return True
    return False
