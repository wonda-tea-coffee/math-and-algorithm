def product(m):
    if m == 0:
        return 0
    ans = 1
    while m >= 1:
        ans *= (m % 10)
        m //= 10
    return ans

def g(a, b):
    if b == 11:
        fc.add(product(a))
        return
    m = a % 10
    for i in range(m, 10):
        g(a * 10 + i, b + 1)

N, B = list(map(int, input().split()))
ans = 0
fc = set()
g(0, 0)

for fci in fc:
    m = fci + B
    if m - product(m) == B and m <= N:
        ans += 1

print(ans)
