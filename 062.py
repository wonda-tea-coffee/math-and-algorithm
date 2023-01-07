N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
A.insert(0, -1)

i = 1
path = [i]
h = { i: True }
t = None
while True:
    if h.get(A[i], False):
        t = path.index(A[i])
        break
    else:
        h[A[i]] = True
        path.append(A[i])
    i = A[i]

# print(path)
# print("t:", t, ", path[t]:", path[t])

if len(path) > K:
    print(path[K])
else:
    # print("K - t:", K - t)
    # print("len(path) - t:", len(path) - t)
    print(path[(K - t) % (len(path) - t) + t])
