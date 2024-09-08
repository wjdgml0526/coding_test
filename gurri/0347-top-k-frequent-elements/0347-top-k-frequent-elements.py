from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)
        
        # 'k' most freq ? - 가장 많이 나오는 k개 ? 
        print(s)
        return sorted(s, key=lambda x: s[x], reverse=True)[:k]

