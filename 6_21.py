import math

def f(x):
    return math.e ** x

# f'(x)
def fp(x):
    return math.e ** x

# 適当な初期値
a = 1
# math.log(r, e)の近似値を求める
r = 2

for i in range(10):
    t = fp(a)
    b = f(a) - t * a
    # y = tx + b と y = r の交点を求める
    # tx + b = 2
    # tx = r - b
    x = (r - b) / t

    print("Step #%2i: a = %.16f -> %.16f" % (i + 1, a, x))

    a = x

print("ans:", math.log(r, math.e))
