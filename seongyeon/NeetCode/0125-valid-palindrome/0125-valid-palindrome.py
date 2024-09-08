class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub('[^a-z0-9]','', s)
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                return False
        return True
        