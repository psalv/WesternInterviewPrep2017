
import math

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "(" + str(self.start) + ", " + str(self.end) + ")"


# Merge sort modified to look at the start of the element
def mergeSort(toSort):
    n = int(len(toSort))


    if n <= 1:
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

        if l1[i].start >= l2[j].start:
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
        merged = []
        for i in elements:
            if merged == []:
                print(i)
                merged.append(i)
            else:
                print(i)
                if i.start <= merged[-1].end:
                    merged[-1].end = max(merged[-1].end, i.end)
                else:
                    merged.append(i)

        return merged


def test():
    a = Interval(1, 4)
    b = Interval(1, 5)

    intervals = [a, b]

    print(Solution.merge(Solution(), intervals))


test()
