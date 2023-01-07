H, W = list(map(int, input().split()))
B = [None] * H

for i in range(H):
    B[i] = list(map(int, input().split()))

row = [0] * H
col = [0] * W
for hi in range(H):
    for wi in range(W):
        row[hi] += B[hi][wi]
        col[wi] += B[hi][wi]

res = [0] * W
for hi in range(H):
    for wi in range(W):
        res[wi] = row[hi] + col[wi] - B[hi][wi]

    print(' '.join(map(str, res)))
