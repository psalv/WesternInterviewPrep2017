
def mergeSort(ar):
    if len(ar) <= 1:
        return ar

    l = mergeSort(ar[:int(len(ar) // 2)])
    r = mergeSort(ar[int(len(ar) // 2):])

    return merge(l, r)


def merge(a1, a2):
    new = []

    pos1 = 0
    pos2 = 0

    while len(new) < len(a1) + len(a2):

        if pos1 >= len(a1):
            new += a2[pos2:]

        elif pos2 >= len(a2):
            new += a1[pos1:]

        elif a1[pos1] < a2[pos2]:
            new.append(a1[pos1])
            pos1 += 1

        else:
            new.append(a2[pos2])
            pos2 += 1

    return new


print(mergeSort([1, 4, 3, 3, 5, 45, 24, 23, 12, 4, 656]))
