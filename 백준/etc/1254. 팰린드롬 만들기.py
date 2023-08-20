S = input()

idx = len(S)-1

i = 0
while i<len(S)-1:

  if S[i] == S[idx]:
    idx = idx - 1
  elif idx != len(S)-1:
    idx = len(S)-1
  i = i+1

print(i + idx + 1)
