def find_number_k(array, i, j, k):
    cut_array = array[i-1:j]
    sorted_array = sorted(cut_array)
    number_k = sorted_array[k-1]
    
    return number_k

def solution(array, commands):
    answer = []
    for element_array in commands:
        answer.append(find_number_k(array, element_array[0], element_array[1], element_array[2])) 
    
    return answer

# 참고 : 리스트의 슬라이싱 https://wikidocs.net/14#_4 - 갑자기 생각 안 났음...ㅎ
# 참고 : list.sort()와 sorted(list) 차이 https://inma.tistory.com/137