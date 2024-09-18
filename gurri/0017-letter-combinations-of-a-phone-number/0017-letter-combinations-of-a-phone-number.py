class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            # after search, backtracking
            if len(path) == len(digits):
                result.append(path)
                return
            
            # repeat input digit unit
            for i in range(index, len(digits)):
                # repeat all strings of num
                for j in dic[digits[i]]:
                    dfs(i+1, path+j)

        # exception
        if not digits:
            return []

        dic = {"2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"}

        result = []
        dfs(0, "")

        return result