class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        count = defaultdict(int)
        pl = 0
        maxf = 0
        for pr in range(len(s)):
            count[s[pr]] += 1
            maxf = max(maxf, count[s[pr]])

            if (pr - pl + 1) - maxf > k:
                count[s[pl]] -= 1
                pl += 1
        
        return (pr - pl + 1)