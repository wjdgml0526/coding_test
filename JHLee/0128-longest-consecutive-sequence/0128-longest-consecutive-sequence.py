class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        consec_dict = defaultdict(int)
        max_len = 0
        for n in nums:
            if n in consec_dict:
                continue
            
            if (n - 1) in consec_dict:
                consec_dict[n] = consec_dict[n - 1] + 1
            else:
                consec_dict[n] = 1
            
            if max_len < consec_dict[n]:
                max_len = consec_dict[n]
        return max_len