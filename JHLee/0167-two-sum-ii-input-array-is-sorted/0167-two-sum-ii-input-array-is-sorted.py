class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        lp = 0
        rp = len(numbers) - 1
        while lp < rp:
            if numbers[lp] + numbers[rp] == target:
                return [lp + 1, rp + 1]
            elif numbers[lp] + numbers[rp] < target:
                lp += 1
            else:
                rp -= 1