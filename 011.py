n = int(input())

def is_prime(m):
    if m == 1 or m > 2 and m % 2 == 0:
        return False

    d = 3
    while d * d <= m:
        if m % d == 0:
            return False
        d += 2

    return True

primes = []
for i in range(1, n + 1):
    if is_prime(i):
        primes.append(i)

print(' '.join(map(str, primes)))
