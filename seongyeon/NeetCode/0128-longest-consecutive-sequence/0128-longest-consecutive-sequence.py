class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        nums = sorted(nums)
        result = 0
        cnt = 1
        for i in range(1, len(nums)):
            tmp = nums[i] - nums[i-1]
            if tmp <= 1:
                cnt += tmp
            else:
                if cnt > result:
                    result = cnt
                cnt = 1
        return max(result, cnt)
        