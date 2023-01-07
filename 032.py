import sys

N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

A.sort()

result = False
left = 0
right = N - 1
while left <= right:
    mid = (right + left) // 2
    if A[mid] == X:
        print("Yes")
        sys.exit(0)
    elif A[mid] < X:
        left = mid + 1
    else:
        right = mid - 1

print("No")
