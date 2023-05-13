short = []
for _ in range(9):
    short.append(int(input()))
short.sort()

sum = sum(short)
trg = sum-100

flag = False
l = len(short)
for i in range(l):
    for j in range(l):
        if i==j:
            pass
        else:
            if short[i]+short[j]==trg:
                tmp = short[j]
                short.remove(short[i])
                short.remove(tmp)
                flag = True
                break
    if flag==True:
        for height in short:
            print(height)
        break