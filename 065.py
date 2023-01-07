H, W = list(map(int, input().split()))

if H == 1 or W == 1:
    print(1)
elif H % 2 == 0 or W % 2 == 0:
    print(H * W // 2)
else:
    a = (H + 1) // 2
    b = (W + 1) // 2
    print(2 * a * b - a - b + 1)
