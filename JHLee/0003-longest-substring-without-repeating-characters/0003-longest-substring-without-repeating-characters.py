class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_idx = defaultdict(int)
        chars = set()
        max_len = 0
        cur_len = 0
        pl = 0
        for pr, string in enumerate(s):
            if string in chars:
                max_len = max(max_len, cur_len)
                pl = char_idx[string]
                cur_len = pr - pl
                chars = set(s[pl + 1: pr + 1])
                char_idx[string] = pr
            else:
                cur_len += 1
                char_idx[string] = pr
                chars.add(string)
        return max(max_len, cur_len)