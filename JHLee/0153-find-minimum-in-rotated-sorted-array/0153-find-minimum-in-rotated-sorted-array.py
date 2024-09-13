class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lp, rp = 0, len(nums) - 1
        while lp <= rp:
            idx = lp + ((rp - lp) // 2)
            if nums[lp] > nums[rp]:
                lp = idx + 1
            elif nums[lp] <= nums[rp]:
                return nums[lp]