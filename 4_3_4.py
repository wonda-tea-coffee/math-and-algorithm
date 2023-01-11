l = 1
r = 2
for i in range(100):
    m = (l + r) / 2
    if m*m*m*m*m*m*m*m*m*m < 1000:
        l = m
    else:
        r = m
    print("Step #%2i: %.16f" % (i+1, m))
