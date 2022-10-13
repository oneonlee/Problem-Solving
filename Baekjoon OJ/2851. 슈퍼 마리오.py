mushrooms_list = []
for _ in range(10):
    user_input = int(input())
    mushrooms_list.append(user_input)

score=0
i=0
while i<10:
    if abs(score-100)>=abs(score+mushrooms_list[i]-100):
        score+=mushrooms_list[i]
        i+=1
    else:
        break

print(score)
