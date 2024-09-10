class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        fp = 0
        bp = len(s) - 1
        while fp < bp:
            if not (s[fp].isalpha() or s[fp].isnumeric()):
                fp += 1
                continue
            if not (s[bp].isalpha() or s[bp].isnumeric()):
                bp -= 1
                continue
            
            if s[fp].lower() != s[bp].lower():
                return False
            else:
                fp += 1
                bp -= 1

        else:
            return True