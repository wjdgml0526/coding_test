class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        result = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            
            if i > 0 and nums[i - 1] == n:
                continue
            
            lp = i + 1
            rp = len(nums) - 1
            while lp < rp:
                tmp_sum = n + nums[lp] + nums[rp]
                if tmp_sum == 0:
                    result.append([n, nums[lp], nums[rp]])
                    rp -= 1
                    lp += 1
                elif tmp_sum > 0:
                    rp -= 1
                else:
                    lp += 1

        return result