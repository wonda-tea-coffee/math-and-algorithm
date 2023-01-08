def factorial(n, m):
    ret = 1
    for i in range(1, n + 1):
        ret = ret * i % m
    return ret

def modpow(a, b, m):
    ret = 1
    k = a
    while b > 0:
        if b & 1:
            ret = ret * k % M
        k = k**2 % M
        b //= 2

    return ret

X, Y = list(map(int, input().split()))
M = 1000000007

a = factorial(X + Y, M)
b = factorial(X, M) * factorial(Y, M) % M

print(a * modpow(b, M - 2, M) % M)
