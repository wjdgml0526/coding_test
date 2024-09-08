class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def backtracking(paren, op, cl):
            if len(paren) == 2 * n:
                res.append(paren)
            else:
                if op < n:
                    backtracking(paren + "(", op + 1, cl)
                if cl < op:
                    backtracking(paren + ")", op, cl + 1)

        backtracking("", 0, 0)

        return res
        