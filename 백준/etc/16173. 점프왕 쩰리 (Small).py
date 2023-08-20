N = int(input())

game_board = []
for _ in range(N):
    game_board.append([int(map) for map in input().split()])

curr  = {'row' = 0, 'col' = 0}

while (True):
    if curr['row']<0 or curr['row']>=N or curr['col']<0 or curr['col']>=N:
        print("OUT!!!!!!!!!!!!!!!!!!!!!!")
        break
    if curr['row']=N-1 and curr['col']=N-1:
        print("HaruHaru")
    movable = game_board[curr['row']][curr['col']]
    
    
    
