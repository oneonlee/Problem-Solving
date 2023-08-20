import re

def judge(new_id):
    # step1
    new_id = new_id.lower()
    
    # step2
    new_id = re.sub('[~!@#$%^&*()=+[{}:?,<>/\\\\\]]', '', new_id)
    
    # step3
    result = ""
    result += new_id[0]
    for i in range(1, len(new_id)):
        if new_id[i-1]==".":
            if new_id[i-1] != new_id[i]:
                result += new_id[i]
                # print("if")
        else:
            result += new_id[i]
            # print("else")
    new_id = result

    # step4
    if len(new_id) > 1:
        while new_id[0] == ".":
            new_id = new_id[1:]
        while new_id[-1] == ".":
            new_id = new_id[:-1]
    elif new_id == ".":
        new_id = ""
    
    # step5
    if new_id == "":
        new_id = "a"
        
    # step6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        while new_id[-1] == ".":
            new_id = new_id[:-1]
    
    # step7
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]
        
    return new_id


def solution(new_id):
    answer = judge(new_id)
    return answer