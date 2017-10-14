
class Solution(object):

    def recursiveSearch(self, nums, target):

        if len(nums) == 0:
            return -1

        middle = int(len(nums) / 2)

        if nums[0] == target:
            return 0
        if nums[-1] == 0:
            return len(nums) - 1

        currentValue = nums[middle]

        if currentValue == target:
            return middle

        if currentValue > target:
            if nums[0] > target:
                if currentValue < nums[0]:
                    return self.recursiveSearch(nums[:middle], target)
                else:
                    cur = self.recursiveSearch(nums[middle + 1:], target)
                    if cur == -1:
                        return cur
                    else:
                        return cur + middle
            else:
                cur = self.recursiveSearch(nums[middle + 1:], target)
                if cur == -1:
                    return cur
                else:
                    return cur + middle
        else:
            if nums[0] > currentValue:
                if currentValue < nums[0]:
                    return self.recursiveSearch(nums[:middle], target)
                else:
                    cur = self.recursiveSearch(nums[middle + 1:], target)
                    if cur == -1:
                        return cur
                    else:
                        return cur + middle
            else:
                return self.recursiveSearch(nums[:middle], target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        length = len(nums) - 1
        if length < 0:
            return -1

        return self.recursiveSearch(nums, target)


# vals = [4, 5, 6, 7, 8, 0, 1, 2, 3]
# vals = [7,8,1,2,3,4,5,6]
# vals = [4,5,6,7,0,1,2]
# vals =[1, 3]
# print(Solution.search(Solution(), vals, 5))
# Solution.search(Solution(), vals, 7)
