class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        t = [] 
        for n in nums:
            if n in t:
                return True
            else:
                t.append(n)
        return False
    
################################################

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False