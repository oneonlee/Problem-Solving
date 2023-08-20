n = int(input())

fibo = [0 for i in range(n + 1)]

fibo[1] = 1

if n>1:
  fibo[2] = 2

if n>2:
  for i in range(3, n + 1):
      fibo[i] = (fibo[i - 1] + fibo[i - 2])%10007

print(fibo[n])