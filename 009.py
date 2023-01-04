n, s = list(map(int, input().split()))
a = list(map(int, input().split()))

def solve(i, sum):
    if sum == s:
        return True
    if i >= n or sum > s:
        return False

    return solve(i + 1, sum) or solve(i + 1, sum + a[i])

if solve(0, 0):
    print("Yes")
else:
    print("No")
