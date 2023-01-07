N = int(input())
A = list(map(int, input().split()))

dp = [0] * N
dp[0] = A[0]
dp[1] = A[1]

for i in range(2, N):
    dp[i] = max(dp[i - 2] + A[i], dp[i - 1])

print(dp[N - 1])
