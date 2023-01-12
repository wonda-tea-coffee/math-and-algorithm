N = int(input())

f = [1] * (N+1)
for i in range(2, N+1):
    j = i
    while j <= N:
        f[j] += 1
        j += i

ans = 0
for i in range(1, N+1):
    ans += i * f[i]

print(ans)
