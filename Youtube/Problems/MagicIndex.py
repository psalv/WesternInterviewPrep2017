

def findMagicIndex(ar):
    """
    Take a sorted array and find an index s.t. ar[i] = i
    """
    left = 0
    right = len(ar) - 1

    while left <= right:
        cur = (left + right) // 2

        if ar[cur] == cur:
            return cur

        elif ar[cur] > cur:
            right = cur - 1

        else:
            left = cur + 1

    return -1


def test():
    x = [-3, -2, 1, 3]
    print(findMagicIndex(x))


test()

