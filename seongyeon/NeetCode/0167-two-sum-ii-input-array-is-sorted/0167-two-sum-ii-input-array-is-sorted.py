class Solution(object):
    def twoSum(self, num, k):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(num) - 1
        while i < j:
            sm = num[i] + num[j]
            if sm == k:
                return [i + 1, j + 1]
            elif sm > k:
                j -= 1
            else:
                i += 1
        return []