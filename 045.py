from collections import deque

N, M = list(map(int, input().split()))
G = [[] for i in range(N+1)]

for i in range(M):
    A, B = list(map(int, input().split()))
    if A > B:
        G[A].append(B)
    elif A < B:
        G[B].append(A)

ans = 0
for i in G:
    if len(i) == 1:
        ans += 1

print(ans)
