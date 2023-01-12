from collections import deque

N, M = list(map(int, input().split()))
G = [[] for i in range(N+1)]
P = [-1] * (N+1)

for i in range(M):
    A, B = list(map(int, input().split()))
    G[A].append(B)
    G[B].append(A)

queue = deque([(1, 0)])

while len(queue) > 0:
    position, step = queue.popleft()
    # print("position: %i / step: %i" % (position, step))
    # print(P)

    if P[position] == -1:
        P[position] = step
    else:
        continue

    for i in G[position]:
        if P[i] == -1:
            queue.append((i, step + 1))

for i in range(1, N+1):
    print(P[i])
