# https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())

num = a*b*c

count_array=[0 for i in range (10)]

for i in range (1, len(str(num))+1):

  index_num = (num%(10**i) - num%(10**(i-1)))//(10**(i-1))
  # print(i, num, 10**i, index_num)

  count_array[index_num]+=1

for sum in count_array:
  print(sum)
