
import time

#
def fib(i):
    """
    O(n), dynamically computes, using prev and cur as the memo (can throw away other unneeded values)
    """
    if i < 2:
        return 1

    prev = 1
    cur = 1

    for i in range(i - 1):
        temp = cur
        cur = prev + cur
        prev = temp

    return cur


def recFib(i):
    """
    O(n!) recursive solution
    """
    if i < 2:
        return 1

    return recFib(i - 2) + recFib(i - 1)


def testFib(n):

    print("DP:")
    start = time.time()
    for i in range(0, n):
        print(i)
        fib(i)
    time1 = time.time() - start

    print("\nRecursive:")
    start = time.time()
    for i in range(0, n):
        print(i)
        recFib(i)
    time2 = time.time() - start

    print('\nDP:{t1}, Rec:{t2}'.format(t1=time1, t2=time2))


testFib(36)
