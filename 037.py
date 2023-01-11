import sys

def cross(x1, y1, x2, y2):
    return x1 * y2 - y1 * x2

x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
x3, y3 = list(map(int, input().split()))
x4, y4 = list(map(int, input().split()))

c1 = cross(x2 - x1, y2 - y1, x3 - x1, y3 - y1) # cross(vec(AB), vec(AC))
c2 = cross(x2 - x1, y2 - y1, x4 - x1, y4 - y1) # cross(vec(AB), vec(AD))
c3 = cross(x4 - x3, y4 - y3, x1 - x3, y1 - y3) # cross(vec(CD), vec(CA))
c4 = cross(x4 - x3, y4 - y3, x2 - x3, y2 - y3) # cross(vec(CD), vec(CB))

# すべてが一直線上に並んでいるケース
if c1 == 0 and c2 == 0 and c3 == 0 and c4 == 0:
    A = (x1, y1)
    B = (x2, y2)
    C = (x3, y3)
    D = (x4, y4)
    if A > B:
        A, B = B, A
    if C > D:
        C, D = D, C
    if max(A, C) <= min(B, D):
        print("Yes")
    else:
        print("No")
    sys.exit(0)

isAB = (c1 >= 0 and c2 <= 0) or (c1 <= 0 and c2 >= 0)
isCD = (c3 >= 0 and c4 <= 0) or (c3 <= 0 and c4 >= 0)

if isAB and isCD:
    print("Yes")
else:
    print("No")
