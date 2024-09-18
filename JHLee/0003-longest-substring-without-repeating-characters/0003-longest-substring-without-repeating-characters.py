class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        pl = 0
        max_len = 0
        for pr in range(len(s)):
            while s[pr] in charSet:
                charSet.remove(s[pl])
                l += 1
            charSet.add(s[pr])
            max_len = max(max_len, pr - pl + 1)
        return max_len