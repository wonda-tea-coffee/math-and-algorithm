n = int(input())
a = list(map(int, input().split()))
h = {}
c = {}

for i in range(0, n):
    if a[i] in h:
        h[a[i]] += 1
    else:
        h[a[i]] = 1
        c[a[i]] = False

ans = 0
TARGET = 100000
for i in h:
    if (not TARGET - i in h) or c.get(i, True):
        continue

    if TARGET - i == i:
        ans += h[i] * (h[i] - 1) // 2
    else:
        ans += h[i] * h[TARGET - i]

    c[TARGET - i] = True

print(ans)
