N = int(input())
A = list(map(int, input().split()))
A.sort()
A.insert(0, -1)
sum = [0] * (N + 1)
sum[1] = A[1]
for i in range(2, N + 1):
    sum[i] = sum[i - 1] + A[i]

ans = 0
for i in range(1, N + 1):
    ans += i * A[i] - sum[i]

print(ans)
