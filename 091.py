N, X = map(int, input().split())

ans = 0
for a in range(1, N + 1):
    for b in range(a + 1, N + 1):
        c = X - a - b
        if b < c and c <= N:
            # print(a, b, c)
            ans += 1

print(ans)
