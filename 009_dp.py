N, S = list(map(int, input().split()))
A = list(map(int, input().split()))
M = 10001
dp = [[False for j in range(M)] for i in range(N)]
dp[0][0] = True
dp[0][A[0]] = True

for i in range(1, N):
    for j in range(M):
        if dp[i - 1][j]:
            dp[i][j] = True

            if j + A[i] <= S:
                dp[i][j + A[i]] = True

if dp[N - 1][S]:
    print("Yes")
else:
    print("No")
