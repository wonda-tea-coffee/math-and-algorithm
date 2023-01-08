N = int(input())
A = list(map(int, input().split()))

ans = 0
k = 1
for ai in A:
    ans += ai * k % 1000000007
    k = k * 2 % 1000000007

print(ans % 1000000007)
