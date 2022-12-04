n = int(input())

L = []
for i in range(n):
    L.append(int(input()))
    
L.sort(reverse=True)

for i in L:
    print(i)