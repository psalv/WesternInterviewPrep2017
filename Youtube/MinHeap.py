

def heapify(ar):
    for i in range(len(ar) - 1, -1, -1):
        ar = minheapify(ar, i)
    return ar


def minheapify(ar, i):
    l = 2*i + 1
    r = 2*i + 2

    if l >= len(ar):
        return ar

    smallest = i
    if ar[l] < ar[i]:
        smallest = l

    if r < len(ar) and ar[r] < ar[smallest]:
        smallest = r

    if smallest != i:
        temp = ar[i]
        ar[i] = ar[smallest]
        ar[smallest] = temp

        return minheapify(ar, smallest)

    else:
        return ar


def testHeapify():
    testArray = [-230, 12, 1, 12, 5, 6, 7, 68, -123, 32, 1]
    print(heapify(testArray))


testHeapify()
