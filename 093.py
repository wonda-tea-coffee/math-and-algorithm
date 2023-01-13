def gcd(a, b):
    if a < b:
        a, b = b, a

    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

A, B = map(int, input().split())

l = lcm(A, B)
if l > 10**18:
    print("Large")
else:
    print(l)
