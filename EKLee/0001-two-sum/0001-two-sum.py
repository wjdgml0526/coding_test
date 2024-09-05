class Solution(object):
    def twoSum(self, nums, target):
        table = {}
        ## hash table 저장
        ## 
        for i, num in enumerate(nums):
            complement = target - num
            if complement in table:
                return [i, table[complement]]
            else:
                table[num] = i