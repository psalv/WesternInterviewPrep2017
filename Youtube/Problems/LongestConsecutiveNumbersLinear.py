

# The key to this problem was that items in the center are never looked at again.
# So when we need to update the new sizes, we actually only need to update the sizes of the extremities,
# which will be at most two sides.
class Solution(object):

    @staticmethod
    def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numMap = {}
        for n in nums:
            if not (n in numMap):
                left = 0
                if n - 1 in numMap:
                    left = numMap[n - 1]

                right = 0
                if n + 1 in numMap:
                    right = numMap[n + 1]

                numMap[n] = left + right + 1

                numMap[n - left] = numMap[n]
                numMap[n + right] = numMap[n]

        maxNum = 0
        for i in numMap:
            if numMap[i] > maxNum:
                maxNum = numMap[i]
        return maxNum


print(5 == Solution.longestConsecutive([234, 3, 123980, 4, 201938, 1, 828, 2, 99, 5]))
