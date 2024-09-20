class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while (l < r):
            # 갱신
            maxArea = max(maxArea, (r - l)* min(
                height[l], height[r]
            ))

            # 이동
            if height[l] < height[r] : l+= 1
            else : r -= 1

        return maxArea