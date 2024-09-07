from functools import reduce

class Solution(object):
    def multiply(self, arr):
        return reduce(lambda x,y : x*y, arr)

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        result = 1
        for i in range(n):
            ans.append(result)
            result *= nums[i]
        
        result = 1
        for i in reversed(range(n)):
            ans[i] *= result
            result *= nums[i]

        return ans 