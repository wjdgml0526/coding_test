class Solution:
    def isPalindrome(self, s: str) -> bool:

        res = "".join([
<<<<<<< HEAD
            c for c in s if c.isalnum()
        ]).lower()
=======
            c.lower() for c in s if c.isalnum()
        ])
>>>>>>> upstream/main

        return True if res == res[::-1] else False