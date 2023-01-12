sum = 0
N = 1000000
for i in range(1, N+1):
    x = (2 * i - 1) / (2 * N)
    sum += 2**(x**2)

print("sum / N: %.16f" % (sum / N))
print("    ans: 1.2882263643059391")
