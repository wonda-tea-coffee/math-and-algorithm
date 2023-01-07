N, K = list(map(int, input().split()))

sum = 0
for r in range(1, N + 1):
    for w in range(max(1, r - K + 1), min(N + 1, r + K)):
        for b in range(max(1, r - K + 1), min(N + 1, r + K)):
            if abs(w - b) < K:
                # print(r, w, b)
                sum += 1

print(N**3 - sum)
