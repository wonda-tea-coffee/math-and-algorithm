n = int(input())

d = 2
m = n
divisors = []

while d * d <= n:
    while m % d == 0:
        divisors.append(d)
        m //= d
    d += 1

if m > 1:
    divisors.append(m)

print(' '.join(list(map(str, divisors))))
