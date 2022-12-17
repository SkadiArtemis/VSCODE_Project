class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        
        for i in range(k):
            while len(q) != 0:
                if nums[i] > nums[q[-1]]:
                    q.pop()
                else:
                    break
            q.append(i)
            
        for i in range(k, len(nums)):
            res.append(nums[q[0]])
            
            if q[0] < i - k + 1:
                q.popleft()
            
            while len(q) != 0:
                if nums[i] > nums[q[-1]]:
                    q.pop()
                else:
                    break
            q.append(i)
        
        res.append(nums[q[0]])
        return res