# https://docs.python.org/3/library/functions.html#bin
# https://wikidocs.net/121166
# https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%84%EC%88%98%EB%B3%80%ED%99%982%EC%A7%84%EB%B2%95-3%EC%A7%84%EB%B2%95-5%EC%A7%84%EB%B2%95-10%EC%A7%84%EB%B2%95n%EC%A7%84%EB%B2%95
# https://www.daleseo.com/python-int-bases/
# http://egloos.zum.com/mataeoh/v/7117043

A = input() # ex> 0001011000
B = input() # ex> 0000101111

# N = max(len(A), len(B))
N = 100000

A = int(A, 2)
B = int(B, 2)

mask = 2 ** N - 1

# print("{0:b}".format(A&B).zfill(N))
# print("{0:b}".format(A|B).zfill(N))
# print("{0:b}".format(A^B).zfill(N))
# print("{0:b}".format(A^mask).zfill(N))
# print("{0:b}".format(A^mask).zfill(N))
# print("{0:b}".format(~A).zfill(N))
# print("{0:b}".format(~B).zfill(N))

print(bin(A&B)[2:].zfill(N))
print(bin(A|B)[2:].zfill(N))
print(bin(A^B)[2:].zfill(N))
# print(bin(~A)[2:].zfill(N))
# print(bin(~B)[2:].zfill(N))
print(bin(A^mask)[2:].zfill(N))
print(bin(B^mask)[2:].zfill(N))
