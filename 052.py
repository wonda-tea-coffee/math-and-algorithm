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

def comb(n, r , m):
    a = factorial(n, m)
    b = factorial(r, m) * factorial(n - r, m) % m
    return a * modpow(b, m - 2, m) % m

X, Y = list(map(int, input().split()))
M = 1000000007
if X < Y:
    temp = Y
    Y = X
    X = temp

if (X + Y) % 3 == 0 and X / Y <= 2:
    Z = (X + Y) // 3
    print(comb(Z, Y - Z, M))
else:
    print(0)
