N = int(input())
A = list(map(int, input().split()))
M = int(input())

D = [0] * (N - 1)
D[0] = A[0]
for i in range(1, N - 1):
    D[i] = D[i - 1] + A[i]

ans = 0
s = int(input()) - 2
for i in range(M - 1):
    t = int(input()) - 2
    if s < t:
        ans += D[t]

        if s >= 0:
            ans -= D[s]
    elif s > t:
        ans += D[s]

        if t >= 0:
            ans -= D[t]
    s = t

print(ans)
