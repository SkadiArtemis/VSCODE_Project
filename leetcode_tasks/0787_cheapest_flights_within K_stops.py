from collections import defaultdict, deque
class Solution:
    # fixed BFS solution by putting accumulated distance with node, so accumulated distance won't be affected by other operations
    def findCheapestPrice_BFS(self, n, flights, src, dst, K):
        edges = defaultdict(dict)
        for u, v, p in flights:
            edges[u][v] = p
        
        INT_MAX = 2**31 - 1
        prices = [INT_MAX]*n

        q = deque([(src, 0)])
        while q and K > -1:
            m = len(q)
            for _ in range(m):
                i, p = q.popleft()
                if p < prices[i]:
                    prices[i] = p
                    for j in edges[i]:
                        q.append((j, p+edges[i][j]))
            
            K -= 1
        
        return -1 if prices[dst] == INT_MAX else prices[dst]

    # Another BFS solution that copies the previous dist array and then do BFS level scan
    def findCheapestPrice_BFS2(self, n, flights, src, dst, K):
        edges = defaultdict(dict)
        for u, v, p in flights:
            edges[u][v] = p
        
        INT_MAX = 2**31 - 1
        prices = [INT_MAX]*n
        prices[src] = 0

        q = deque([src])
        while q and K > -1:
            m = len(q)
            t = prices[:]   # make a copy of previous price array
            for _ in range(m):
                u = q.popleft()
                for v in edges[u]:
                    new_price = t[u] + edges[u][v]
                    if new_price < prices[v]:
                        prices[v] = new_price
                        q.append(v)
            
            K -= 1
        
        return -1 if prices[dst] == INT_MAX else prices[dst]

    # my own BFS solution, failed on test case flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], n = 4, src = 0, dst = 3, K = 1
    def findCheapestPrice_Wrong(self, n, flights, src, dst, K):
        edges = defaultdict(dict)
        for u, v, p in flights:
            edges[u][v] = p
        
        INT_MAX = 2**31 - 1
        prices = [INT_MAX]*n
        prices[src] = 0

        q = deque([src])
        while q and K > -1:
            m = len(q)
            for _ in range(m):
                i = q.popleft()
                for j in edges[i]:
                    if prices[i] + edges[i][j] < prices[j]: # this is the issue. prices[i] may have been updated by other routes in this level of BFS scan, see above test case. We need to save the prices of i in queue so it won't be updated by following other routes
                        prices[j] = prices[i] + edges[i][j]
                        q.append(j)
            
            K -= 1
        
        return -1 if prices[dst] == INT_MAX else prices[dst]

    # DFS solution, TLE
    def findCheapestPrice_DFS(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        edges = defaultdict(dict)
        for u, v, p in flights:
            edges[u][v] = p
        self.res = 2**31 - 1

        def dfs(i, k, p):
            if k > K + 1:
                return
            if i == dst:
                self.res = min(self.res, p)
                return
            for j in edges[i]:
                dfs(j, k+1, p + edges[i][j])

        dfs(src, 0, 0)

        return -1 if self.res == 2**31 - 1 else self.res

    # Bellman Ford algorithm from http://www.cnblogs.com/grandyang/p/9109981.html
    def findCheapestPrice(self, n, flights, src, dst, K):
        INT_MAX = 2**31 - 1
        dp = [[INT_MAX]*n for _ in range(K+2)]  # dp[i][j] is the lowest price flying i times to location j
        dp[0][src] = 0
        for i in range(1, K+2):
            dp[i][src] = 0
            for u, v, p in flights:
                dp[i][v] = min(dp[i][v], dp[i-1][u] + p)    # minimum betwee current lowest price, and last location + price from last location to this

        return -1 if dp[K+1][dst] >= INT_MAX else dp[K+1][dst]

#n, src, dst, K = 3, 0, 2, 1
#flights = [[0,1,100],[1,2,100],[0,2,500]]
n=4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst=3
K=1

print(Solution().findCheapestPrice_DFS(n, flights, src, dst, K))