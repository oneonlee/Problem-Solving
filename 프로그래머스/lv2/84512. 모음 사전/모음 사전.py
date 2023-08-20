def solution(target_word):
    
    dict_list = []
    first_alphabet_list = ["A", "E", "I", "O", "U"]
    alphabet_list = ["", "A", "E", "I", "O", "U"]
    

    for first_alphabet in first_alphabet_list:
        word = first_alphabet
        for alphabet2 in alphabet_list:
            word2 = word
            word2 += alphabet2
            if alphabet2 == "":
                dict_list.append(word2)
                pass
            
            for alphabet3 in alphabet_list:
                word3 = word2
                word3 += alphabet3
                if alphabet3 == "":
                    dict_list.append(word3)
                    pass
                
                for alphabet4 in alphabet_list:
                    word4 = word3
                    word4 += alphabet4
                    if alphabet4 == "":
                        dict_list.append(word4)
                        pass
                    
                    for alphabet5 in alphabet_list:
                        word5 = word4
                        word5 += alphabet5
                        dict_list.append(word5)

    dict_list = list(set(dict_list))
    dict_list.sort()
    # print(dict_list)
    answer = dict_list.index(target_word) + 1
    return answer