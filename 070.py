N, K = list(map(int, input().split()))
L = []
C = []
for i in range(N):
    xi, yi = list(map(int, input().split()))
    L.append((xi, yi))

for i in L:
    for j in L:
        for k in L:
            for l in L:
                cl, cr, dl, dr = i[0], j[0], k[1], l[1]
                cnt = 0
                for m in L:
                    if cl <= m[0] and m[0] <= cr and dl <= m[1] and m[1] <= dr:
                        cnt += 1

                if cnt >= K:
                    C.append((cl - cr) * (dl - dr))

print(min(C))
