class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        i = 0
        j = len(height) -1
    
        while i < j:
            l = j - i
            area = max(area, min(height[i], height[j]) * l)
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return area
         
