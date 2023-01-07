N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

sum = 0
for ai in A:
    sum += ai

if sum <= K and sum % 2 == K % 2:
    print("Yes")
else:
    print("No")
