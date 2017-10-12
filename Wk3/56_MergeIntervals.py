
import math

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def getStart(self):
        return self.start

    def __repr__(self):
        return "(" + str(self.start) + ", " + str(self.end) + ")"


# Merge sort modified to look at the start of the element
def mergeSort(toSort):
    n = int(len(toSort))


    if n == 1:
        return toSort

    new1 = mergeSort(toSort[0: int(math.floor(n / 2))])
    new2 = mergeSort(toSort[int(math.floor(n / 2)):])

    return merge(new1, new2)


def merge(l1, l2):
    ans = []
    n1, n2 = len(l1), len(l2)

    i, j = 0, 0
    while len(ans) < n1 + n2:

        if j == n2:
            ans += l1[i:]
            return ans
        if i == n1:
            ans += l2[j:]
            return ans

        if l1[i].getStart() >= l2[j].getStart():
            ans.append(l2[j])
            j += 1
        else:
            ans.append(l1[i])
            i += 1


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        elements = mergeSort(intervals)
        print(elements)



def test():
    a = Interval(1, 3)
    b = Interval(2, 6)
    c = Interval(8, 10)
    d = Interval(15, 18)

    intervals = [c, a, b, d]

    Solution.merge(Solution(), intervals)

test()