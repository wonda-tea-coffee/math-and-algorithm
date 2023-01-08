a, b = list(map(int, input().split()))
M = 1000000007

ans = 1
k = a

while b > 0:
    if b & 1:
        ans = ans * k % M
    k = k**2 % M
    b //= 2

print(ans)
