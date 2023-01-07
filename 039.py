N, Q = list(map(int, input().split()))
sum = [0] * N

for i in range(Q):
    L, R, X = list(map(int, input().split()))
    if L > 1:
        sum[L - 1] -= X
    if R < N:
        sum[R] += X

ans = ''
for i in range(1, N):
    if sum[i] < 0:
        ans += '<'
    elif sum[i] > 0:
        ans += '>'
    else:
        ans += '='

print(ans)
