N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(0, N):
    ans += 2 * A[i] + 4 * B[i]

print(ans / 6)
