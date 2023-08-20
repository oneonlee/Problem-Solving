N = int(input())

cost = []

for i in range(N):
    a,b,c = input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    cost.append([a,b,c])

dp = cost.copy()
for i in range(1, N):
    for j in range(3):
        if j==0:
            dp[i][j] = cost[i][j] + min(dp[i-1][1], dp[i-1][2])
        elif j==2:
            dp[i][j] = cost[i][j] + min(dp[i-1][0], dp[i-1][1])
        else:
            dp[i][j] = cost[i][j] + min(dp[i-1][j-1], dp[i-1][j+1])

print(min(dp[N-1]))