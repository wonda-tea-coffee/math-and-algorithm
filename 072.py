import math

A, B = list(map(int, input().split()))

ans = 0
for i in range(1, B + 1):
    if B // i - math.ceil(A / i) >= 1:
        ans = i

print(ans)
