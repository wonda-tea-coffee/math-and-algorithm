a, b, c, d = list(map(int, input().split()))

res = []
for a in [[a, c], [a, d], [b, c], [b, d]]:
    res.append(a[0] * a[1])

print(max(res))
