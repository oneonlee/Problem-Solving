n=45

nums = []
for i in range(n+1):
    for j in range(i):
        nums.append(i)
        
        
a, b = input().split()
a = int(a)
b = int(b)

sum = 0
for i in range(a, b+1):
    sum+=nums[i-1]

print(sum)