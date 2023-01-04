def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)

a, b = list(map(int, input().split()))
print(gcd(a, b))
