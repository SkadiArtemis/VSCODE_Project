class DSU(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
            self.rank[yr] += self.rank[xr]
        else:
            self.parent[yr] = xr
            self.rank[xr] += self.rank[yr]

        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        dsu = DSU(len(edges) + 1)
        for start, end in edges:
            if not dsu.union(start, end):
                return [start, end]