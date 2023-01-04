def pick2(n):
    return n * (n - 1) // 2

n = int(input())
a = list(map(int, input().split()))

count = {}
for i in range(0, n):
    if a[i] in count:
        count[a[i]] += 1
    else:
        count[a[i]] = 1

a1 = count.get(1, 0)
a2 = count.get(2, 0)
a3 = count.get(3, 0)
print(pick2(a1) + pick2(a2) + pick2(a3))
