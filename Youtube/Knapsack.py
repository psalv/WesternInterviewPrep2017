

class Item(object):
    def __init__(self, i, v, w):
        self.item = i
        self.value = v
        self.weight = w


def solveKnapsack(items, W):
    memo = []
    for i in range(len(items)):
        memo.append([])
        for j in range(W):
            memo[i].append(0)

    # Work from left to right, and then go down the rows
    for i in range(len(items)):
        for w in range(W):

            # Pull from the top if we are over weight
            if items[i].weight > w:
                memo[i][w] = memo[i - 1][w]

            # Take the max of:
            #   - taking the current item and then adding that to the max weight of our reduced weight threshold
            #   - not taking this weight and just pulling down
            else:
                memo[i][w] = max(items[i].value + memo[i - 1][w - items[i].weight], memo[i - 1][w])

            print(i, w)
            print(memo)
            print()

    return memo[len(items) - 1][w - 1]


def testKnapsack():
    a = Item("a", 1, 3)
    b = Item("b", 2, 6)
    c = Item("c", 8, 1)
    d = Item("d", 7, 20)

    print(solveKnapsack([a, b, c, d], 9))


testKnapsack()


