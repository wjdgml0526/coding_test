from functools import reduce

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        new_nums =[]
        for i in range(len(nums)):
            new_nums.append(nums[:i] + nums[i+1:])
        result = []
        for i in range(len(nums)):
            result.append(reduce(lambda x, y: x * y, new_nums[i]))

        return result