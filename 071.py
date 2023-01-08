N = int(input())
A = []
B = []
C = []
for i in range(N):
    a, b, c = list(map(int, input().split()))
    A.append(a)
    B.append(b)
    C.append(c)

T = []
for i in range(N):
    for j in range(i + 1, N):
        if A[j] * B[i] == A[i] * B[j]:
            continue

        x = (B[i] * C[j] - B[j] * C[i]) / (A[j] * B[i] - A[i] * B[j])
        y = (A[j] * C[i] - A[i] * C[j]) / (A[j] * B[i] - A[i] * B[j])

        is_ok = True
        for k in range(N):
            if A[k] * x + B[k] * y > C[k]:
                is_ok = False
                break

        if is_ok:
            T.append(x + y)

print(max(T))
