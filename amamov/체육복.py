def solution(n, lost, reserve):
    _lost = [i for i in lost if i not in reserve]
    _reserve = [i for i in reserve if i not in lost]
    wow = 0
    for i in _lost:
        for j in _reserve:
            if i == j-1 or i == j+1:
                wow +=1
                _reserve.remove(j)
                break
    return n - len(_lost) + wow
