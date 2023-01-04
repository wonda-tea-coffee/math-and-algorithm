def comb(n, r):
    if n < r:
        return 0
    elif r == 0:
        return 1
    elif r == 1:
        return n
    else:
        return comb(n - 1, r - 1) + comb(n - 1, r)

n, r = list(map(int, input().split()))
print(comb(n, r))
