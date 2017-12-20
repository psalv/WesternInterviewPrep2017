

def mxnSearch(matrix, i):

    m = len(matrix)
    n = len(matrix[0])

    low = 1
    high = m - 2

    row = None
    while low <= high:
        middle = (low + high) // 2

        if matrix[middle - 1][0] <= i < matrix[middle][0]:
            row = middle - 1
            break

        elif matrix[middle][0] <= i < matrix[middle + 1][0]:
            row = middle
            break

        elif matrix[middle][0] < i:
            low = middle + 1

        else:
            high = middle - 1

    if row is None:
        row = m - 1

    low = 0
    high = n - 1

    col = None
    while low <= high:
        middle = (low + high) // 2

        if matrix[row][middle] == i:
            col = middle
            break

        elif matrix[row][middle] < i:
            low = middle + 1

        else:
            high = middle - 1

    if col is None:
        return None

    return row, col


def test():

    x = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]

    for i in range(22):
        print(mxnSearch(x, i))


test()

