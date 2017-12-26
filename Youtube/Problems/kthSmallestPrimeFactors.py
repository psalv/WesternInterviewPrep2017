

def listOfMultiples(k):
    nums = []

    I = []
    for i in range(1, k + 1):
        I.append(3 ** i)

    J = []
    for i in range(1, k + 1):
        J.append(5 ** i)

    L = []
    for i in range(1, k + 1):
        L.append(7 ** i)

    for i in I:
        for j in J:
            for l in L:
                nums.append(i * j * l)

    return sorted(nums)[k - 1]


def withoutList(k):
    toAdd = (k + 1) // 8
    k %= 6
    nums = [[1, 1, 1], [2, 1, 1], [1, 2, 1], [1, 1, 2], [2, 2, 1], [1, 2, 2]]
    cur = nums[k - 1]

    return 3 ** (cur[0] + toAdd) * 5 ** (cur[1] + toAdd) * 7 ** (cur[2] + toAdd)


# Find the kth smallest number with only prime factors of 3, 5, and 7
def test():
    # print(listOfMultiples(10))
    for i in range(1, 11):
        print("\n", i)
        print(withoutList(i))


test()
