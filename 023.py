N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

ans = 0
for i in range(0, N):
    ans += B[i] + R[i]

print(ans / N)

# (1+10)/9 + (1+20)/9 + (1+30)/9 + ... + (3+30)/9
# = {(1+10)+(1+20)+(1+30)+...+(3+30)}/9
# = 3(1+2+3+10+20+30)/9
# = (1+2+3+10+20+30)/3
