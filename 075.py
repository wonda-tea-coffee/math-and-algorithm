def modpow(a, b, m):
    ret = 1
    k = a
    while b > 0:
        if b & 1:
            ret = ret * k % M
        k = k**2 % M
        b //= 2

    return ret

def comb(n, r, m):
    a = fact[n]
    b = fact[r] * fact[n - r] % m
    return a * modpow(b, m - 2, m) % m

N = int(input())
A = list(map(int, input().split()))
M = 1000000007

fact = [0] * N
fact[0] = 1
for i in range(1, N):
    fact[i] = i * fact[i - 1] % M

ans = 0

for i in range(N):
    ans = (ans + A[i] * comb(N - 1, i, M)) % M

print(ans)
