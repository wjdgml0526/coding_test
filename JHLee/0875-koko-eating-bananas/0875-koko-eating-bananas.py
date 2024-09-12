class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        piles = sorted(piles)
        k = 1
        while k <= piles[-1]:
            time = 0
            for pile in piles:
                time += (pile // k) + 1 if (pile % k) > 0 else pile // k
            if time == h:
                return k
            else:
                k += 1