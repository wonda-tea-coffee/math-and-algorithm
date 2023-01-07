N, W = list(map(int, input().split()))
w = [0] * N
v = [0] * N
for i in range(N):
    w[i], v[i] = list(map(int, input().split()))

dp = [[-1 for j in range(W + 1)] for i in range(N)]

dp[0][0] = 0
dp[0][w[0]] = v[0]
for i in range(1, N):
    for j in range(0, W + 1):
        if dp[i - 1][j] < 0:
            continue

        #print(i, j)
        dp[i][j] = max(dp[i][j], dp[i - 1][j])

        if j + w[i] <= W:
            dp[i][j + w[i]] = max(dp[i][j + w[i]], dp[i - 1][j] + v[i])

ans = 0
for i in range(W + 1):
    ans = max(ans, dp[N - 1][i])

print(ans)
