n = int(input())
a = list(map(int, input().split()))

count = {}
for i in range(0, n):
    if a[i] in count:
        count[a[i]] += 1
    else:
        count[a[i]] = 1

print(count.get(100, 0) * count.get(400, 0) + count.get(200, 0) * count.get(300, 0))
