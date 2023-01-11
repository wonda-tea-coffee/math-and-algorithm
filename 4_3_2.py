r = 2
a = 2

for i in range(10):
    x = a
    y = a ** 3

    a = 3 * x**2 # f'(x)
    b = y - a * x
    na = (r - b) / a
    print("Step #%2i: a = %.16f -> %.16f" % (i+1, a, na))

    a = na
