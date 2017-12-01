
import math


def nchoosek(n, k):
    """
    n
    k   =   n! / ( k! * (n - k)! )

    The amount of ways that we can select k elements from a pool of n elements

    So there are n! different permutation of n
    There are k! different permutations that we can find since we are not looking at order
    """
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def testMath():
    print(3 == nchoosek(3, 1))
    print(3 == nchoosek(3, 2))
    print(1 == nchoosek(3, 3))
    print(6 == nchoosek(4, 2))


testMath()
