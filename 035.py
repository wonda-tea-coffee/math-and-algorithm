import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

x1, y1, r1 = list(map(int, input().split()))
x2, y2, r2 = list(map(int, input().split()))

d = distance(x1, y1, x2, y2)

if d > r1 + r2:
    print(5)
elif d == r1 + r2:
    print(4)
elif d + r1 == r2 or d + r2 == r1:
    print(2)
elif d + r1 < r2 or d + r2 < r1:
    print(1)
else:
    print(3)
