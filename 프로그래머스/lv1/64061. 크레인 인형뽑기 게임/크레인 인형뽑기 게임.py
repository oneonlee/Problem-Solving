def solution(board, moves):
    # moves로부터 크레인을 작동시킬 위치를 불러온다.
    # 위치를 토대로 크레인을 작동시킨다.
    # 작동시킬 때에, basket 배열에 옮겨진 인형을 담는다.
    # 마지막에, basket 배열을 검사함으로서, answer를 도출해낸다.

    # 예외처리하기 : 비어 있는 곳에 크레인을 작동시키는 경우 (헛발질)

    basket =[]
    
    for turn in range(0, len(moves)):  # turn은 몇번째 실행(턴)인지를 나타내는 변수
        target_col = moves[turn] # 크레인이 내려갈 목표 지점의 열
        for row in range(0, len(board)):
            current_doll_info = board[row][target_col - 1] # 현재 크레인이 있는 곳의 인형의 정보
            if current_doll_info != 0:  # 인형의 모양이 0이 아니면
                basket.append(current_doll_info) # basket 배열에 담는다.
                board[row][target_col - 1] = 0 # 원래 자리에 있던 인형을 없애준다. 
                break

    # judge part
    answer = 0
    
    i = 0
    while i < len(basket):
        try:
            if basket[i]==basket[i + 1]:
                answer += 2
                del basket[i+1]
                del basket[i]
                i = 0
            else:
                i = i + 1
        except IndexError:
            break
            
    return answer


# 참고 : 반복문으로 2차원 리스트의 요소를 모두 출력하기 https://dojang.io/mod/page/view.php?id=2292
# 참고 : range를 사용하여 리스트 만들기 https://dojang.io/mod/page/view.php?id=2200h
# 참고 : 리스트 요소 제거 https://wikidocs.net/14#remove
# 참고 : 리스트 뒤집기(reverse) https://wikidocs.net/14#reverse
# 참고 : del 함수 사용해 리스트 요소 삭제하기 https://wikidocs.net/14#del
# 참고 : for문 range에서 숫자를 감소시키기 https://dojang.io/mod/page/view.php?id=1271