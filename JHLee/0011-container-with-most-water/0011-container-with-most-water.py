class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        max_amount = 0
        for i in range(len(height)):
            for j in range(len(height) - 1, i, -1):
                amount = min(height[i], height[j]) * (j - i)
                max_amount = max(max_amount, amount)
        
        return max_amount