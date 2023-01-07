T = int(input())
N = int(input())
d = [0] * T
cnt0 = 0

for i in range(N):
    L, R = list(map(int, input().split()))

    if L == 0:
        cnt0 += 1
    elif L > 0:
        d[L] += 1
    if R < T:
        d[R] -= 1

# print(d)

for i in range(T):
    cnt0 += d[i]
    print(cnt0)
