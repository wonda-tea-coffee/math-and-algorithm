N, X, Y = list(map(abs, map(int, input().split())))

if N >= X + Y and (N - X - Y) % 2 == 0:
    print("Yes")
else:
    print("No")
