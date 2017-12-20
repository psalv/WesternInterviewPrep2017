

def binarySearch(ar, i):
    left = 0
    right = len(ar) - 1

    while left <= right:
        middle = (left + right) // 2
        if ar[middle] == i:
            return middle

        if ar[middle] > i:
            right = middle - 1
        else:
            left = middle + 1

    return -1


def testSearchAlgorithm():
    x = [1, 34, 465, 898998, 23939393]

    print(0 == binarysearch(x, 1))
    print(1 == binarysearch(x, 34))
    print(4 == binarysearch(x, 23939393))
    print(-1 == binarysearch(x, 0))
    print(-1 == binarysearch(x, 23939394))

    print(-1 == binarysearch([], 1))


testSearchAlgorithm()
