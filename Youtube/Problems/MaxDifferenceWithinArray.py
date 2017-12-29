
class Solution(object):

    @staticmethod
    def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        length = len(prices)
        maxDiff = 0
        maxRight = length - 1

        for i in range(length - 2, -1, -1):
            if prices[i] > prices[maxRight]:
                maxRight = i

            if prices[maxRight] - prices[i] > maxDiff:
                maxDiff = prices[maxRight] - prices[i]

        return maxDiff


print(Solution.maxProfit([23, 12, 188, 89, 12321, 90, 100]))
