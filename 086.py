import sys

N = int(input())
S = input()

l, r = 0, 0
for si in S:
    if si == "(":
        l += 1
    elif si == ")":
        r += 1

    if l < r:
        print("No")
        sys.exit(0)

print("Yes")
