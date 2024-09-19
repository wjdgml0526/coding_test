class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            max_profit = max(max_profit, price - lowest)
        return max_profit