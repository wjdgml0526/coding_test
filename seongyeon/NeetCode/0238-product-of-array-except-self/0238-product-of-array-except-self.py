from functools import reduce

class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def multiply(arr):
            return reduce(lambda x,y : x*y, arr)
            
        result = []
        all_ = multiply(nums)
        if nums.count(0) >= 1:
            ans = [0 for _ in range(len(nums))]
            if nums.count(0) == 1:
                i = nums.index(0)
                ans[i] = multiply(nums[:i] + nums[i+1 :])
            return ans
        else:
            return [all_ //n for n in nums]
            



            tmp = nums[:i] + nums[i+1 :]
            result.append(multiply(tmp))
        return result
            