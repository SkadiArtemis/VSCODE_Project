class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        INF = 0x3F3F3F3F
        n = len(points)
        g = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    g[i][j] = abs(x1 - x2) + abs(y1 - y2)
        dist = [INF] * n
        vis = [False] * n
        ans = 0
        for i in range(n):
            t = -1
            for j in range(n):
                if not vis[j] and (t == -1 or dist[t] > dist[j]):
                    t = j
            if i:
                ans += dist[t]
            for j in range(n):
                dist[j] = min(dist[j], g[t][j])
            vis[t] = True
        return ans