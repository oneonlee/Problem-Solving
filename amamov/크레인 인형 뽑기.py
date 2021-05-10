def pong(container):
    while True:
        isFinish = True
        for idx in range(len(container)-1, 0, -1):
            if container[idx] == container[idx-1]:
                del container[idx]
                del container[idx-1]
                isFinish = False
                break
        if isFinish:
            break
    return container
        

def solution(board, moves):
    length = len(board)
    moves = [i - 1 for i in moves]
    container = []
    for move_idx in moves:
        for i in range(length):
            doll = board[i][move_idx]
            if doll != 0:
                container.append(doll)
                board[i][move_idx] = 0
                break

    answer = len(container) - len(pong(container))
    return answer
