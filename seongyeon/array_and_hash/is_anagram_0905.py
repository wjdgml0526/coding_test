from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt= 0
        if len(s) != len(t):
            return False

        if Counter(s) == Counter(t):
            return True
        return False
    
##################################################
# Solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT