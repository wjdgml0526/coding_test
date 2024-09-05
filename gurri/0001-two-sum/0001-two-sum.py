class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, val1 in enumerate(nums):
            for j, val2 in enumerate(nums):
                if i == j :
                    continue
                
                if val1 + val2 == target:
                    return (i, j)
        