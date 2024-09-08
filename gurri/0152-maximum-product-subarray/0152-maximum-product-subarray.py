class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        """
        subarray - Nonempty sequence
        2, 3 = 6
        2, 3, -2 = -12
        2, 3, -2, 4 = -48
        3, -2 = -6
        3, -2, 4 = -24
        -2, 4 = -8
        """

        ans = max(nums)
        curMin, curMax = 1, 1

        for num in nums:
            if num == 0 : 
                curMin, curMax = 1, 1
                continue
            
            tmp = num * curMax
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            ans = max(ans, curMax)

        return ans