import math

N = int(input())

k = math.log(N + 1, 2)
if k == int(k):
    print("Second")
else:
    print("First")
