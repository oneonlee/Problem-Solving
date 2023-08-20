def isPrime(num):
    cnt = 0
    for i in range(1, num+1):
        if num%i == 0:
            cnt+=1
    if cnt==2:
        return True
    else:
        return False

N = int(input())
num_list = [int(x) for x in input().split()]

prime_cnt = 0
for num in num_list:
    if isPrime(num)==True:
        prime_cnt+=1

print(prime_cnt)
