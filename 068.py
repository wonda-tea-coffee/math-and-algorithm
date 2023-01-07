import math

def _lcm(a, b):
    return a * b // math.gcd(a, b)

def lcm(a):
    ret = 1
    for ai in a:
        ret = _lcm(ret, ai)
    return ret

N, K = list(map(int, input().split()))
V = list(set(list(map(int, input().split()))))
K = len(V)
ans = 0
for i in range(1, 2**K):
    a = []
    t = 0
    for j in range(K):
        if (i >> j) & 1:
            t += 1
            a.append(V[j])
    if t % 2:
        ans += N // lcm(a)
    else:
        ans -= N // lcm(a)

print(ans)
