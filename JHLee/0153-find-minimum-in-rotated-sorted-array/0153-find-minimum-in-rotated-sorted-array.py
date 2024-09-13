class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lp, rp = 0, len(nums) - 1
        while lp <= rp:
            if nums[lp] > nums[rp]:
                lp += 1
            elif nums[lp] < nums[rp]:
                rp -= 1
            else:
                return nums[lp]