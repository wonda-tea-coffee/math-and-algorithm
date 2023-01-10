import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

N = int(input())
T = []
S = []
for i in range(N):
    T.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i + 1, N):
        S.append(distance(T[i][0], T[i][1], T[j][0], T[j][1]))

print(min(S))
