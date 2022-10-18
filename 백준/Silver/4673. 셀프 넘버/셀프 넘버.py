def d(n):
    result = n
    
    while True:
        if n<1:
            return result
        else:
            result+=n%10
            n=n//10
            

answer = [i for i in range(1, 10001)]
d_list = []
for i in range(1, 10000):
    d_list.append(d(i))


answer = list(set(answer) - set(d_list))
answer.sort()

for self_num in answer:
    print(self_num)