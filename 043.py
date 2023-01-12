def dfs(n):
    C.add(n)

    for i in G[n]:
        if i not in C:
            dfs(i)

N, M = list(map(int, input().split()))
G = [[] for i in range(N+1)]
C = set()

for i in range(M):
    A, B = list(map(int, input().split()))
    G[A].append(B)
    G[B].append(A)

stack = [1]

while len(stack) > 0:
    s = stack.pop()

    C.add(s)
    for i in G[s]:
        if i not in C:
            stack.append(i)

if len(C) == N:
    print("The graph is connected.")
else:
    print("The graph is not connected.")
