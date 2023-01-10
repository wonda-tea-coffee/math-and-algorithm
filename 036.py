import math

A, B, H, M = list(map(int, input().split()))

D = abs((60*H - 11*M) / 720)

print(math.sqrt(A * A + B * B - 2 * A * B * math.cos(D * 2 * math.pi)))
