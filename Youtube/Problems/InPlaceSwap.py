

def inplaceswap(ar, i, j):
    ar[j] += ar[i]
    ar[i] = ar[j] - ar[i]
    ar[j] -= ar[i]
    return ar


def test():
    print(inplaceswap([1, 2, 3, 4, 5, 6, 7], 1, 5))


test()


