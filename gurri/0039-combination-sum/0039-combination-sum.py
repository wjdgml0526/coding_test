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

        def backtrack(idx, cur):
            # 기저조건
            if cur > target :
                return 
            
            # 조건 만족 시 추가 
            if cur == target :
                result.add(tuple(sorted(selected[:])))
                return
            
            for i in range(len(candidates)):
                if cur <= target :
                    selected.append(candidates[i])
                    backtrack(i, cur + candidates[i])
                    selected.pop()




        result = set()    
        backtrack(0, 0)
        return result
        