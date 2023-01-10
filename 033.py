import math
import sys

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def inner_product(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2

ax, ay = list(map(int, input().split()))
bx, by = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))

bax = ax - bx
bay = ay - by
bcx = cx - bx
bcy = cy - by

if inner_product(bax, bay, bcx, bcy) < 0:
    print(distance(ax, ay, bx, by))
    sys.exit(0)

cax = ax - cx
cay = ay - cy
cbx = bx - cx
cby = by - cy

if inner_product(cax, cay, cbx, cby) < 0:
    print(distance(ax, ay, cx, cy))
    sys.exit(0)

print(abs(bax * bcy - bay * bcx) / distance(bx, by, cx, cy))
