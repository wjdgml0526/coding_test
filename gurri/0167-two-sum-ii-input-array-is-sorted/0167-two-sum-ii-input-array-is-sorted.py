class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1

        while l < r : 
            # l + r 의 합을 target과 비교해서 조정
            if numbers[l] + numbers[r] == target :
                return [l+1, r+1]
            
            elif numbers[l] + numbers[r] < target : 
                l += 1 
            else : 
                r -= 1