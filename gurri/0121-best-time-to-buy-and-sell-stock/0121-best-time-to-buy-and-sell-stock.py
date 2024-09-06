class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        min_price = 9999999999

        for price in prices:
            min_price = min(price, min_price)
            ans = max(ans, price - min_price) 
        return ans 
