import math

A, B, C = list(map(int, input().split()))

if C >= A + B and 4 * A * B < (C - A - B)**2:
    print("Yes")
else:
    print("No")
