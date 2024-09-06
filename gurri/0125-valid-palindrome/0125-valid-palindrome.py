class Solution:
    def isPalindrome(self, s: str) -> bool:

        res = "".join([
            c for c in s if c.isalnum()
        ]).lower()

        return True if res == res[::-1] else False