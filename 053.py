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
M = 1000000007

a = modpow(4, N + 1, M) - 1
b = modpow(3, M - 2, M)
print(a * b % M)
