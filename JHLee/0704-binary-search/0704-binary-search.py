class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        idx = int(round(len(nums) / 2))
        while idx >= 0 and idx < len(nums):
            if nums[idx] == target:
                return idx
            
            prev_idx = idx
            if nums[idx] > target:
                idx = prev_idx - int(round(prev_idx / 2))
            else:
                idx = prev_idx + int(round(prev_idx / 2))
            
            if prev_idx == idx:
                return -1