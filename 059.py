N = int(input()) % 4

# 2^1 % 10 = 2
# 2^2 % 10 = 4
# 2^3 % 10 = 8
# 2^4 % 10 = 6

if N == 1:
    print(2)
elif N == 2:
    print(4)
elif N == 3:
    print(8)
else:
    print(6)
