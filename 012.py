def is_prime(m):
    if m == 1 or m > 2 and m % 2 == 0:
        return False

    d = 3
    while d * d <= m:
        if m % d == 0:
            return False
        d += 2

    return True

if is_prime(int(input())):
    print("Yes")
else:
    print("No")
