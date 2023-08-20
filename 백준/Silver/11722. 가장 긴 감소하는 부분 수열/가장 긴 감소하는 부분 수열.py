# 6
# 10 30 10 20 20 10

N = int(input())
A = list(map(int,input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# 참고
# [Python 1. 입력 받기](https://velog.io/@dlrmwl15/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5%EB%B0%9B%EA%B8%B0)