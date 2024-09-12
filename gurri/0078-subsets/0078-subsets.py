class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Editorial 
        output = [[]] # 공집합은 미리 더해준다.

        for num in nums : 
            newSubsets = []
            for curr in output: # output에서 순회를 한다.
                temp = curr.copy() # 복사하고
                temp.append(num) # 수 추가하고
                newSubsets.append(temp) # 추가한 결과를 부분집합에 추가하고
            for curr in newSubsets: # 새로 만들어진 것에서 순회를 하는데
                output.append(curr) # 결과물을 추가하기
        return output




        # -----my solution -----#         
        # selected = []
        # visited = [False for _ in range(len(nums))]
        # ans = []
        # ans_set = set()

        # # on/off 0, 1 / length 0, 1, 2
        # def backtracking(cnt):
        #     if cnt == len(nums):
        #         tmp = sorted(selected.copy())
        #         if tuple(tmp) not in ans_set :
        #             ans.append(tmp)
        #             ans_set.add(tuple(tmp))
        #         return
            
        #     # cnt : 뽑고/안뽑고 여부를 시행하는 횟수
        #     for idx in range(cnt, len((nums))) :
        #         if sorted(selected) not in ans : 
        #             if not visited[idx]:
        #                 selected.append(nums[idx])
        #                 visited[idx] = True
        #                 backtracking(cnt+1)
        #                 selected.pop()
        #                 visited[idx] = False
        #                 backtracking(cnt+1)

        # backtracking(0)
        # print(ans)
        # return ans