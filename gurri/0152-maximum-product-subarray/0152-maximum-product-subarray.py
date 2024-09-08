class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        forward = nums[::]
        backward = nums[::-1]

        for i in range(1, len(nums)):
            forward[i] *= forward[i-1] or 1
            backward[i] *= backward[i-1] or 1

        return max(forward+backward)