

def makeCents(n, memo=None):
    """

    This solves when the order that the coin is taken out is relevent
    So for instance in this situation there are 4 ways to make 7 cents:

        1 1 5
        1 5 1
        5 1 1
        1 1 1 1 1 1 1

    """

    if n == 0:
        return 1

    # maps cents to number of ways to make it
    if memo is None:
        memo = []
        for i in range(n + 1):
            memo.append(0)

    if memo[n] == 0:

        cents = [1, 5, 10, 25]

        for c in cents:
            if n - c >= 0:

                memo[n] += makeCents(n - c, memo)
                print(memo)

    return memo[n]


def test():
    # print(" 1: ", 1 == makeCents(1))
    # print(" 2: ", 1 == makeCents(2))
    # print(" 5: ", 2 == makeCents(5))
    # print(" 6: ", 2 == makeCents(6))
    # print("10: ", 4 == makeCents(10))

    print(makeCents(7))


test()
