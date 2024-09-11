class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        nums = sorted(nums)
        while i < len(nums):
            if nums[i] > i:
                break
            i += 1
        return i
        