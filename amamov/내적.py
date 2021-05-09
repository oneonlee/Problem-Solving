def solution(a, b):
    dot_product = 0
    length = len(a)
    for i in range(length):
        dot_product += a[i]*b[i]
    return dot_product
