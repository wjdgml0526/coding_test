import heapq

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''
        Prices = [7, 1, 5, 3, 6, 4]
        Output: 5
        
        given an array "prices" - prices[i] given stock on the ith day.
        choosing a different day in the future to sell that stock.

        Maximum profit / not achieve - 0

        Two pointer ? 
        - must buy before you sell

        '''
        ans = 0 # maximum profit
        buy = 0
        # sol 1 - O(n2) - Timeout 
        # for i, buy in enumerate(prices):
        #     for j in range(i+1, len(prices)):
        #         # Can sell ? 
        #         if prices[j] > buy : 
        #             gap = prices[j] - buy
        #             # print(gap)
        #             ans = max(gap, ans)

        # Sol2 : for - heapq
        ans = 0

        for i, buy in enumerate(prices):
            sell_candi = list(map(lambda x : -x, prices[i+1:]))

            if i != len(prices) -1 : 
                heapq.heapify(sell_candi)
                sell = -heapq.heappop(sell_candi)

                if buy < sell :
                    ans = max(ans, sell - buy)

        return ans