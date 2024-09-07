class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        nums_freq = defaultdict(int)
        for num in nums:
            nums_freq[num] += 1
        sorted_nums = sorted(nums_freq, key = lambda x: nums_freq[x], reverse = True)
        return sorted_nums[:k]