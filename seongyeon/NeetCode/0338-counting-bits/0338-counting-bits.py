class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n+1):
            cnt = 0
            while i != 0:
                cnt += i % 2
                i = i // 2

            result.append(cnt)
        
        return result
        