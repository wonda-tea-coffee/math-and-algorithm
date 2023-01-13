N = int(input())
score1 = [ 0 ] * (N + 1)
score2 = [ 0 ] * (N + 1)

for i in range(N):
    Ci, Pi = map(int, input().split())
    if Ci == 1:
        score1[i + 1] = Pi
    else:
        score2[i + 1] = Pi

sum1 = [ 0 ] * (N + 1)
sum2 = [ 0 ] * (N + 1)
sum1[1] = score1[1]
sum2[1] = score2[1]
for i in range(2, N + 1):
    sum1[i] = sum1[i - 1] + score1[i]
    sum2[i] = sum2[i - 1] + score2[i]

Q = int(input())
# print("sum:")
# print(sum1, sum2)
for i in range(Q):
    Li, Ri = map(int, input().split())
    print(sum1[Ri] - sum1[Li - 1], sum2[Ri] - sum2[Li - 1])
