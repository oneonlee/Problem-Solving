input()
L = list(map(int, input().split()))
L = list(set(L))
L.sort()

for i in L:
    print(i)