N = int(input())
ans = 0
for i in range(0, N):
    Pi, Qi = list(map(int, input().split()))
    ans += 2520 / Pi * Qi

# 2^3 * 3^2 * 5 * 7 = 2520

print(ans / 2520)
