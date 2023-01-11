import math

ans = math.sqrt(2)

def match_count(a, b):
    ret = 0
    sa = str(a - int(a))
    sb = str(b - int(b))
    i = 2
    while i < min(len(sa), len(sb)) and sa[i] == sb[i]:
        ret += 1
        i += 1

    return ret

l = 1
r = 2
i = 1
while True:
    m = (l + r) / 2
    if m**2 < 2:
        l = m
    else:
        r = m
    print("Step #%2i: %.15f" % (i, m))

    if match_count(ans, m) == 6:
        break
    i += 1
