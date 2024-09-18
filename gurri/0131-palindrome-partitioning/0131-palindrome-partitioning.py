class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        selected = []

        # 부분문자열 중 palindrome 만을 반환
        def backtracking(idx):
            if idx >= len(s):
                print(selected)
                return
            
            for i in range(idx, len(s)):

                selected.append(i)
                backtracking(i+1)
                selected.pop()
                backtracking(i+1)


        backtracking(0)


