N = int(input())

d = 1
ans = 10**13
while d * d <= N:
    if N % d == 0:
        ans = min(ans, 2 * (d + N // d))
    d += 1
print(ans)
