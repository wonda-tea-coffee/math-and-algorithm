import sys

N, X, Y = list(map(int, input().split()))
L = 300

for a in range(1, L + 1):
    for b in range(1, L + 1):
        for c in range(1, L + 1):
            d = X - a - b - c
            if d >= 1 and d <= L and a * b * c * d == Y:
                print("Yes")
                sys.exit(0)

print("No")
