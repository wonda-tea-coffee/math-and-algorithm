n = int(input())
a = list(map(int, input().split()))

def dfs(i, cnt, sum):
    if cnt == 5 and sum == 1000:
        return 1
    if i >= n or cnt == 5 or sum > 1000:
        return 0

    return dfs(i + 1, cnt, sum) + dfs(i + 1, cnt + 1, sum + a[i])

print(dfs(0, 0, 0))
