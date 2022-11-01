def foo(L, P, V):
    if V%P>L:
        return(V//P*L+L)
    else:
        return(V//P*L+V%P)


test = []
while True:
    case = [int(i) for i in input().split()]
    if case==[0, 0, 0]:
        break
    test.append(case)

for i in range(len(test)):
    print(f"Case {i+1}: {foo(test[i][0], test[i][1], test[i][2])}")