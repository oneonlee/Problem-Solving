N = int(input())
count = 0
minimum=[N]
def cal(n):
    list = []
    for i in n:
        list.append(i-1)
        if i%3 == 0:
            list.append(i/3)
        if i%2 == 0:
            list.append(i/2)
    return list
 
while True:
    if N == 1:
        print(count)
        break
    temp = minimum
    minimum = []
    minimum = cal(temp)
    count +=1
    # print(minimum)
    # print(min(minimum))
    if min(minimum) == 1:
        print(count)
        break