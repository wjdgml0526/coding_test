class Solution:
    def isPalindrome(self, s: str) -> bool:

        res = "".join([
            c.lower() for c in s if c.isalnum()
        ])

        return True if res == res[::-1] else False