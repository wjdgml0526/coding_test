class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count_s1 = [0] * 26
        window = [0] * 26
        for i in range(len(s1)):
            idx = ord(s1[i]) - ord('a')
            count_s1[idx] += 1
            idx = ord(s2[i]) - ord('a')
            window[idx] += 1
        if count_s1 == window:
            return True
        
        pl = 0
        for pr in range(len(s1), len(s2)):
            idx = ord(s2[pl]) - ord('a')
            window[idx] -= 1
            pl += 1
            idx = ord(s2[pr]) - ord('a')
            window[idx] += 1

            if count_s1 == window:
                return True
        return False