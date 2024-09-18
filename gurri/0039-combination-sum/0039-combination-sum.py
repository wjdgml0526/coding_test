class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 수 제한 없이 사용가능 - target를 만드는 수의 조합을 반환
        if not candidates:
            return []

        '''
        2, 3, 5 -> 8? 
        - 2, 2, 2, 2 / 2, 3, 3 / 3, 5
        '''

        selected = []
        n = len(candidates)

        def backtrack(idx, target):
            # 기저조건
            if target == 0:
                result.append(sorted(selected[:]))
            
            # 조건 만족 시 추가 
            if idx == n  or target < 0:
                return
            
            for j in range(idx ,n):
                selected.append(candidates[j])
                backtrack(j, target - candidates[j])
                selected.pop()




        result = []
        backtrack(0, target)
        return result
        