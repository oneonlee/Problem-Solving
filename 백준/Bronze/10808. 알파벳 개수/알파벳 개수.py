al = 'abcdefghijklmnopqrstuvwxyz'

S = input()

for a in al:
    alpha_cnt = 0
    for i in range(len(S)):
        if a==S[i]:
            alpha_cnt+=1
    print(alpha_cnt, end=' ')