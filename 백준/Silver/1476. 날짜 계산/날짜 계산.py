max_E = 15
max_S = 28
max_M = 19

input_E, input_S, input_M = input().split()
input_E = int(input_E)
input_S = int(input_S)
input_M = int(input_M)

# Current
E = 1
S = 1
M = 1
year = 1

while True:
    if E==input_E and S==input_S and M==input_M:
        print(year)
        break
    else:
        year += 1
        if E<max_E:
            E += 1
        else:
            E = 1
        if S<max_S:
            S += 1
        else:
            S = 1
        if M<max_M:
            M += 1
        else:
            M = 1
        