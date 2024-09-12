class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        outputs = [[]]
        
        # 숫자 순회
        for num in nums : 
            newSubsets = []
            
            for curr in outputs :
                tmp = curr.copy()
                tmp.append(num)
                newSubsets.append(tmp)

            for curr in newSubsets :
                if sorted(curr) not in outputs:
                   outputs.append(sorted(curr))

        return outputs