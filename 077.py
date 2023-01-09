N = int(input())
X = []
Y = []
for i in range(N):
    xi, yi = list(map(int, input().split()))
    X.append(xi)
    Y.append(yi)

X.sort()
Y.sort()

X.insert(0, -1)
Y.insert(0, -1)

sumX = [0] * (N + 1)
sumY = [0] * (N + 1)

sumX[1] = X[1]
sumY[1] = Y[1]
for i in range(2, N + 1):
    sumX[i] = sumX[i - 1] + X[i]
    sumY[i] = sumY[i - 1] + Y[i]

ans = 0
for i in range(1, N + 1):
    ans += i * (X[i] + Y[i]) - sumX[i] - sumY[i]

print(ans)
