sum = 0
N = 100000000
for i in range(N):
    sum += 2**((i / N)**2)

print("sum / N: %.16f" % (sum / N))
print("    ans: 1.2882263643059391")
