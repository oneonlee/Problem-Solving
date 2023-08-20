N, M = input().split()
N = int(N)
M = int(M)

A = []
for row in range(N):
    A.append([int(cin) for cin in input().split()])

M, K = input().split()
M = int(M)
K = int(K)

B = []
for row in range(M):
    B.append([int(cin) for cin in input().split()])

AB = [["Default" for col in range(K)] for row in range(N)]
for i in range(N):
    for j in range(K):
        element = 0
        for k in range(M):
            element += A[i][k]*B[k][j]
        AB[i][j] = element

for i in range(N):
    for j in range(K):
        print(AB[i][j], end=' ')
    print()
