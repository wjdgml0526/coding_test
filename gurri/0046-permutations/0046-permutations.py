class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        selected = []
        visited = [False for _ in range(len(nums))]
        ans = []

        def backtracking(cnt):
            if cnt == len(nums):
                print(selected)
                ans.append(selected.copy())
                return
            
            # cnt : 뽑고/안뽑고 여부를 시행하는 횟수
            for idx, val in enumerate(nums):
                if not visited[idx]:
                    selected.append(val)
                    visited[idx] = True
                    backtracking(cnt+1)
                    selected.pop()
                    visited[idx] = False

        backtracking(0)
        print(ans)
        return ans