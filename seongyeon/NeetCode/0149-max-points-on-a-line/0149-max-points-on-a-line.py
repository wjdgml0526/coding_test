class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        n = len(points);
        if n == 1: return 1
        res = 2;
        for i in range(n):
            d = defaultdict(int);
            for j in range(n):
                if i != j:
                    d[math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])] += 1;
            res = max(res, max(d.values()) + 1);
        return res
                    