import sys

a, b, c = list(map(int, input().split()))
M = 10**18
x = 1
k = c
while b > 0:
    # print(k)
    if b & 1:
        x *= k
        if a < x:
            print("Yes")
            sys.exit(0)

    k **= 2
    b //= 2

    if b > 0 and x * k > M:
        print("Yes")
        sys.exit(0)


print("No")
