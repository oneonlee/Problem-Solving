# 6
# 6
# 10
# 13
# 9
# 8
# 1

n = int(input())  # 포도주의 개수
amount = [0]
max_sum = [0]
for i in range(n):
    amount.append(int(input()))
    max_sum.append(0)


if n == 1:
    print(amount[1])

elif n == 2:
    print(amount[1] + amount[2])

else:
    max_sum[1] = amount[1]
    max_sum[2] = amount[1] + amount[2]

    for i in range(3, n + 1):
        # 1. i번째 포도주를 마시는 경우
        ## 1-1. i-1번째 포도주도 마신 경우 (i-2번째 포도주는 안 마심)
        # max_sum[i] = max_sum[i - 3] + amount[i - 1] + amount[i]
        ## 1-2. i-1번째 포도주는 마시지 않은 경우
        # max_sum[i] = max_sum[i - 2] + amount[i]

        # 2. i번째 포도주를 마시지 않는 경우
        # max_sum[i] = max_sum[i - 1]
        
        # 따라서
        max_sum[i] = max(max_sum[i - 3] + amount[i - 1] + amount[i], max_sum[i - 2] + amount[i], max_sum[i - 1])

    print(max_sum[n])
