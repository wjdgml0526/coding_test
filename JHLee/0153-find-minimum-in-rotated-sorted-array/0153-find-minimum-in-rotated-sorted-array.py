class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lp, rp = 0, len(nums) - 1
        min_num = 5001
        while lp <= rp:
            mid = lp + ((rp - lp) // 2)
            min_num = min(min_num, nums[mid])

            if nums[mid] > nums[rp]:
                lp = mid + 1
            else:
                rp = mid - 1
        return min(min_num, nums[lp])