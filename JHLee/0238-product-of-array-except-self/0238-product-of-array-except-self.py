from functools import reduce

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        prev_product = [1] * len(nums)
        post_product = [1] * len(nums)
        for i in range(1, len(nums)):
            prev_product[i] = prev_product[i - 1] * nums[i - 1]
            post_product[- i - 1] = post_product[-i] * nums[-i]
        return [a * b for a, b in zip(prev_product, post_product)]