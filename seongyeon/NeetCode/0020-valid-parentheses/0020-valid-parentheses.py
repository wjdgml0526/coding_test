class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {'(':')','{':'}','[':']'}
        l = []
        for i in s:
            if i in brackets.keys():
                l.append(i)
            elif l == []:
                return False
            elif brackets[l[-1]] == i:
                l.pop(-1)
            else:
                return False
        if l == []:
            return True
        else:
            return False