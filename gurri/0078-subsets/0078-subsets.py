class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        outputs = [[]] # 공집합

        for num in nums : 
            newSubsets = []
            # outputs를 순회하면서 num을 삽입
            for currSubset in outputs : # [] 
                tmp = currSubset.copy() # 복사
                tmp.append(num)          # [num]
                newSubsets.append(tmp)   # [[num]]
            # 결과물 더해주기
            for newSubset in newSubsets:
                outputs.append(newSubset)
        
        return outputs

