N = int(input())

while N!=0:
    test_case = []
    for i in range(N):
        name, height = input().split()
        height = float(height)
        test_case.append((name, height))
    
    test_case.sort(key=lambda x: (x[1]), reverse=True)
    max_height = test_case[0][1]
    
    for name, height in test_case:
        if height==max_height:
            print(name)
        else:
            break
    
    N = int(input())