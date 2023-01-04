import random
import math

def dest(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

N = 1000000
cnt = 0
for i in range(0, N):
    x = random.uniform(0, 6)
    y = random.uniform(0, 9)
    d1 = dest(3, 7, x, y)
    d2 = dest(3, 3, x, y)

    if d1 <= 2 or d2 <= 3:
        cnt += 1

print(cnt)
print(cnt / N * 54) # = 13π(4π + 9π) - ε
