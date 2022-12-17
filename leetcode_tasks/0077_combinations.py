class Solution:
    def combine(self, n, k):
        if k == 1:
            return [[i + 1] for i in range(n)]
        ans = []
        if n > k:
            ans = [i + [n] for i in self.combine(n - 1, k - 1)] \
                  + self.combine(n - 1, k)
        else:
            ans = [i + [n] for i in self.combine(n - 1, k - 1)]
        return ans