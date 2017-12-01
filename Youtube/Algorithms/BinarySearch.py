

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
    numbers = [23, 1, 43, 232, 12, -3, 1, 432, 123, 12]
    numbers = sorted(numbers)

    print(numbers)

    print(binarySearch(numbers, -3))
    print(binarySearch(numbers, 123))
    print(binarySearch(numbers, 432))
    print(binarySearch(numbers, 1230))


testSearchAlgorithm()
