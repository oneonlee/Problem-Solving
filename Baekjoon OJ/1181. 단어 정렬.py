N = int(input())

input_list = []
    
for _ in range(N):
    w = input()
    input_list.append(w)

word_list = list(set(input_list))
word_list.sort()
word_list.sort(key=len)

for word in word_list:
    print(word)
