class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        idx_dict = dict()
        for i in range(len(nums)): 
            prev_idx = idx_dict.get(nums[i], -1)
            if prev_idx >= 0 and i - prev_idx <= k : 
                return True
            idx_dict[nums[i]] = i
        
        return False
