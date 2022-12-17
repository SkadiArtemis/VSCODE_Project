class Solution:
    def arrayChange(self, nums, operations):
	        N = len(operations)
            d = {}
            for i, c in enumerate(nums):
	            d[c] = i
	        for i in range(N):
	            x, y = operations[i]
	            idx = d[x]
	            nums[idx] = y
	            d[y] = idx
	        return nums	