n = int(input())

d = 1
while d * d <= n:
    if n % d == 0:
        print(d)
        if d != n / d:
            print(n // d)
    d += 1
