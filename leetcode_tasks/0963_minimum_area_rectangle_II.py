class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        points = set(map(tuple, points))
        if len(points) < 4:
            return 0
        ans = float('inf')
        for p1, p2, p3 in itertools.permutations(points, 3):
            if ((p2[0] - p1[0]) * (p3[0] - p1[0]) +
                (p2[1] - p1[1]) * (p3[1] - p1[1])) == 0:
                p4 = (p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1])
                if p4 in points:
                    ans = min(math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) *
                              math.sqrt((p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2),
                              ans)
        if ans < float('inf'):
            return ans
        return 0