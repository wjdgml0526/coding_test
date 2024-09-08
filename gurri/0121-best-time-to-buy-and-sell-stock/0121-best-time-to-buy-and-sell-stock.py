<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> upstream/main
<<<<<<< HEAD
=======
>>>>>>> upstream/main
<<<<<<< HEAD
=======
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
>>>>>>> upstream/main
<<<<<<< HEAD
=======
>>>>>>> upstream/main
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
<<<<<<< HEAD
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        min_price = 9999999999

        for price in prices:
            min_price = min(price, min_price)
            ans = max(ans, price - min_price) 
        return ans 
=======
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
<<<<<<< HEAD
=======
>>>>>>> upstream/main
<<<<<<< HEAD
=======
>>>>>>> upstream/main
<<<<<<< HEAD
>>>>>>> upstream/main
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
<<<<<<< HEAD
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> upstream/main
<<<<<<< HEAD
=======
>>>>>>> upstream/main
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
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

        # Sol2 : 역순으로 구하기 
        ans = 0
        max_price = 0

        for price in reversed(prices):
            max_price = max(price, max_price)
            ans = max(ans, max_price - price)

<<<<<<< HEAD
<<<<<<< HEAD
        return ans
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> upstream/main
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
>>>>>>> upstream/main
<<<<<<< HEAD
=======
>>>>>>> upstream/main
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
        return ans
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
>>>>>>> upstream/main
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> upstream/main
<<<<<<< HEAD
=======
>>>>>>> upstream/main
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> upstream/main
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
        return ans
>>>>>>> upstream/main
=======
        return ans
>>>>>>> upstream/main
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
<<<<<<< HEAD
=======
>>>>>>> upstream/main
<<<<<<< HEAD
=======
>>>>>>> upstream/main
<<<<<<< HEAD
>>>>>>> upstream/main
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
<<<<<<< HEAD
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> upstream/main
<<<<<<< HEAD
=======
>>>>>>> upstream/main
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
=======
>>>>>>> upstream/main
