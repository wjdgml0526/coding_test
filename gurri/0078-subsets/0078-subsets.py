class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        selected = []

        def backtracking(curr_idx):
            if curr_idx >= len(nums):
                print(selected)
                ans.append(selected.copy())    
                return

            for i in range(curr_idx, len(nums)):
                if selected not in ans : 
                    selected.append(nums[i])
                    backtracking(i+1)
                    selected.pop()
                    backtracking(i+1)

        backtracking(0)

        return ans