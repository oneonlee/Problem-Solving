def solution(lottos: list, win_nums: list) -> list:
    ranking = lambda x: 7 - x if x != 0 else 6
    h, l = 0, 0
    for lotto in lottos:
        if lotto == 0:
            h += 1
        if lotto in win_nums:
            h += 1
            l += 1
    return [ranking(h), ranking(l)]
