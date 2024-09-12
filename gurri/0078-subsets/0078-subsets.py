class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        selected = []
        visited = [False for _ in range(len(nums))]
        ans = []
        ans_set = set()

        # on/off 0, 1 / length 0, 1, 2
        def backtracking(cnt):
            if cnt == len(nums):
                tmp = sorted(selected.copy())
                if tuple(tmp) not in ans_set :
                    ans.append(tmp)
                    ans_set.add(tuple(tmp))
                return
            
            # cnt : 뽑고/안뽑고 여부를 시행하는 횟수
            for idx in range(cnt, len((nums))) :
                if sorted(selected) not in ans : 
                    if not visited[idx]:
                        selected.append(nums[idx])
                        visited[idx] = True
                        backtracking(cnt+1)
                        selected.pop()
                        visited[idx] = False
                        backtracking(cnt+1)

        backtracking(0)
        print(ans)
        return ans