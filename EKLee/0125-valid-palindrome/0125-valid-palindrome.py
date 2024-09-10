class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in range(0,len(s)):
            if (s[i].isalpha()):
                a=a+s[i].lower()
            elif(s[i].isalnum()):
                a=a+s[i] 
        if (a==a[::-1]):
            return True
        else:
            return False
        