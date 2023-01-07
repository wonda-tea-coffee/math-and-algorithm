N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
sum = [0] * N
sum[0] = A[0]

for i in range(1, N):
    sum[i] = sum[i - 1] + A[i]

for i in range(Q):
    L, R = list(map(int, input().split()))
    if L == 1:
        print(sum[R - 1])
    else:
        print(sum[R - 1] - sum[L - 2])
