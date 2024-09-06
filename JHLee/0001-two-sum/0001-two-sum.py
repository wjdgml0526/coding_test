class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        rests = set()
        rests_dict = {}
        for i, num in enumerate(nums):
            if num > target:
                continue
            
            if num in rests:
                return [rests_dict[num], i]
            else:
                rest = target - num
                rests.add(rest)
                rests_dict[rest] = i
