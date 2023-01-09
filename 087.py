def modpow(a, b, m):
    ret = 1
    k = a
    while b > 0:
        if b & 1:
            ret = ret * k % M
        k = k**2 % M
        b //= 2

    return ret

N = int(input())

print(((N * (N + 1) // 2)**2) % 1000000007)
