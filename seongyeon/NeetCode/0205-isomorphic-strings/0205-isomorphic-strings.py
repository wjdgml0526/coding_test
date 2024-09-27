class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        res={}
        for i in range(0,len(s)):
            if s[i] not in res:
                if t[i] in res.values():
                    return False
                res[s[i]]=t[i]
            if(res[s[i]]!=t[i]):
                return False
        return True       