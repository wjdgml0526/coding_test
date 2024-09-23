class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def backtracking(i, curr):
            if i == len(s):
                ans.append(curr[:])
            
            for j in range(i, len(s)):
                
                if s[i:j+1] == s[i:j+1][::-1]:
                    curr.append(s[i:j+1])
                    backtracking(j+1, curr)
                    curr.pop()


        backtracking(0, [])
        return ans