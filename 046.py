from collections import deque

R, C = list(map(int, input().split()))
M = []
F = [[False for j in range(C)] for i in range(R)]
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))

for i in range(R):
    M.append(input())

queue = deque([(sy-1, sx-1, 0)])

while len(queue) > 0:
    y, x, step = queue.popleft()
    # print("y = %i, x = %i, step = %i" % (y, x, step))

    if y == gy - 1 and x == gx - 1:
        print(step)
        break

    for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny = y + i[0]
        nx = x + i[1]
        if ny >= 0 and ny < R and nx >= 0 and nx < C and not F[ny][nx] and M[ny][nx] == '.':
            F[ny][nx] = True
            queue.append((ny, nx, step + 1))
