T = int(input())

L = []
for _ in range(T):
    R, S = input().split()
    R = int(R)
    L.append([R, S])

for elem in L:
    for i in range(len(elem[1])):
        for _ in range(elem[0]):
            print(elem[1][i], end='')
    print()