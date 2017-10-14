class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        print(nums)

    def wiggleSort2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        even = True
        for i in range(1, len(nums)):
            even = not even
            if even:
                if nums[i - 1] > nums[i]:
                    temp = nums[i - 1]
                    nums[i - 1] = nums[i]
                    nums[i] = temp
            else:
                if nums[i - 1] < nums[i]:
                    temp = nums[i - 1]
                    nums[i - 1] = nums[i]
                    nums[i] = temp

        even = len(nums) % 2 == 0
        for i in range(len(nums) - 2, -1, -1):
            even = not even
            if even:
                if nums[i + 1] > nums[i]:
                    temp = nums[i + 1]
                    nums[i + 1] = nums[i]
                    nums[i] = temp
            else:
                if nums[i + 1] < nums[i]:
                    temp = nums[i + 1]
                    nums[i + 1] = nums[i]
                    nums[i] = temp

        return nums


def test():
    vals = [1,5,1,1,6,4]
    print(Solution.wiggleSort(Solution(), vals))
