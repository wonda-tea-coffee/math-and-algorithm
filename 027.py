N = int(input())
A = list(map(int, input().split()))

def merge_sort(l, r):
    if r - l == 1:
        return

    m = (l + r) // 2
    merge_sort(l, m)
    merge_sort(m, r)

    i1 = l
    i2 = m
    ci = 0
    C = [0] * (r - l)

    while ci < r - l:
        if i1 == m:
            C[ci] = A[i2]
            i2 += 1
        elif i2 == r:
            C[ci] = A[i1]
            i1 += 1
        elif A[i1] < A[i2]:
            C[ci] = A[i1]
            i1 += 1
        else:
            C[ci] = A[i2]
            i2 += 1
        ci += 1

    for i in range(0, r - l):
        A[l + i] = C[i]

merge_sort(0, N)

print(' '.join(map(str, A)))
