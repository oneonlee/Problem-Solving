al = 'abcdefghijklmnopqrstuvwxyz'

S = input()

for a in al:
    isExist = False
    for i in range(len(S)):
        if a==S[i]:
            print(i, end=' ')
            isExist = True
            break
    if isExist == False:
        print(-1)
            