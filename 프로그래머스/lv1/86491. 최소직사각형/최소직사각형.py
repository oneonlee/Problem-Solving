def solution(sizes):
    bigger_list = []
    smaller_list = []
    for size in sizes:
        bigger_list.append(max(size))
        smaller_list.append(min(size))
    
    return max(bigger_list)*max(smaller_list)
